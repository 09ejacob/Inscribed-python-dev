import pygame
from object import Object
from utils import load_sprite_sheets

class Fireball(Object): # pygame.sprite.Sprite
    def __init__(self, x, y, width, height, direction):
        super().__init__(x, y, width, height)
        self.sprites = load_sprite_sheets("Spells", "Fireball", width, height, False)
        self.image = self.sprites["Fireball"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = direction
        self.update_image()

    def update_image(self):
        if self.direction == "left":
            self.image = pygame.transform.flip(self.sprites["Fireball"][0], True, False)
        else:
            self.image = self.sprites["Fireball"][0]
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))

    # def printdir():
    #     print("Direction: ", Player.get_direction())

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
