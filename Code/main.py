import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
from player import Player
from fire import Fire
from block import Block
from utils import load_sprite_sheets, get_block, get_background
from network import Network

pygame.init()
pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.network = Network()
        self.players = {}
        self.run = True
        self.player = None
        self.offset_x = 0

    def draw(self, window, background, bg_image, objects):
        for tile in background:
            window.blit(bg_image, tile)

        for obj in objects:
            obj.draw(window, self.offset_x)

        for player in self.players.values():
            player.draw(window, self.offset_x)

        pygame.display.update()

    def handle_vertical_collision(self, player, objects, dy):
        collided_objects = []
        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    player.landed()
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    player.hit_head()
                collided_objects.append(obj)
        return collided_objects

    def collide(self, player, objects, dx):
        player.move(dx, 0)
        player.update()
        collided_object = None
        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                collided_object = obj
                break
        player.move(-dx, 0)
        player.update()
        return collided_object

    def handle_move(self, player, objects):
        keys = pygame.key.get_pressed()
        player.x_vel = 0

        collide_left = self.collide(player, objects, -PLAYER_VEL * 2)
        collide_right = self.collide(player, objects, PLAYER_VEL * 2)

        if keys[pygame.K_a] and not collide_left:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_d] and not collide_right:
            player.move_right(PLAYER_VEL)

        vertical_collide = self.handle_vertical_collision(player, objects, player.y_vel)
        to_check = [collide_left, collide_right, *vertical_collide]
        for obj in to_check:
            if obj and obj.name == "fire":
                player.make_hit()

    def send_player_data(self):
        data = self.network.send(self.player.to_dict())
        self.players = {int(k): Player.from_dict(v) for k, v in data.items()}

    def main(self):
        background, bg_image = get_background("Blue.png", WIDTH, HEIGHT)
        block_size = 96
        self.player = Player(100, 100, 50, 50, player_id=self.network.id)
        fire = Fire(100, HEIGHT - block_size - 64, 16, 32)
        fire.on()
        floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
        objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size), Block(block_size * 3, HEIGHT - block_size * 4, block_size), fire]

        scroll_area_width = 200

        while self.run:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.player.jump_count < 2:
                        self.player.jump()

            self.player.loop(FPS)
            fire.loop()
            self.handle_move(self.player, objects)
            self.send_player_data()
            self.draw(window, background, bg_image, objects)

            if ((self.player.rect.right - self.offset_x >= WIDTH - scroll_area_width) and self.player.x_vel > 0) or (
                    (self.player.rect.left - self.offset_x <= scroll_area_width) and self.player.x_vel < 0):
                self.offset_x += self.player.x_vel

        pygame.quit()
        quit()

if __name__ == "__main__":
    game = Game()
    game.main()
