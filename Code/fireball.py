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
        self.speed = 10
        self.update_image()

    def update_image(self):
        if self.direction == "left":
            self.image = pygame.transform.flip(self.sprites["Fireball"][0], True, False)
        else:
            self.image = self.sprites["Fireball"][0]
    
        self.mask = pygame.mask.from_surface(self.image)
        #print(self.direction)

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))

    def loop(self):
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed

        # Remove the fireball if it goes off-screen
        if self.rect.right < 0 or self.rect.left > pygame.display.get_surface().get_width():
            self.kill()
            #print("Killed fireball")
            #return
            
        
    def kill_fireball(self):
        self.image = self.sprites["Clear"][0]
        self.kill()


