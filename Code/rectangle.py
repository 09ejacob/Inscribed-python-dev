import pygame

class Rectangle:
    def __init__(self, x, y, width, height, color, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move_forward(self):
        self.rect.x += self.speed
