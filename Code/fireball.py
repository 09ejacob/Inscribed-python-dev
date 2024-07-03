import pygame
from object import Object
from utils import get_block
from utils import load_sprite_sheets

class Fireball(Object): # pygame.sprite.Sprite
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.fireball = load_sprite_sheets("Spells", "Fireball", width, height)
        self.image = self.fireball["Fireball"][0]
        self.mask = pygame.mask.from_surface(self.image)
    
    # def __init__(self, x, y, direction):
    #     super().__init__()
    #     self.image = pygame.Surface((20, 10))
    #     self.image.fill((255, 69, 0))  # Orange color for the fireball
    #     self.rect = self.image.get_rect()
    #     self.rect.center = (x, y)
    #     self.direction = direction
    #     self.speed = 10

    # def update(self):
    #     if self.direction == "right":
    #         self.rect.x += self.speed
    #     elif self.direction == "left":
    #         self.rect.x -= self.speed

    #     # Remove the fireball if it goes off-screen
    #     if self.rect.right < 0 or self.rect.left > pygame.display.get_surface().get_width():
    #         self.kill()
