import pygame

class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((20, 10))
        self.image.fill((255, 69, 0))  # Orange color for the fireball
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.speed = 10

    def update(self):
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed

        # Remove the fireball if it goes off-screen
        if self.rect.right < 0 or self.rect.left > pygame.display.get_surface().get_width():
            self.kill()
