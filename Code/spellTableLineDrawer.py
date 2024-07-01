import pygame

class SpellTableLineDrawer:
    WIDTH = 1000

    def __init__(self):
        self.lines = []
        self.drawing = False
        self.start_pos = (1000 - (64 * 2), 64 * 2)
        self.end_pos = (500, 500)

    def draw(self, window):
        for line in self.lines:
            pygame.draw.line(window, (255, 0, 0), line[0], line[1], 5)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.drawing = not self.drawing
                if self.drawing:
                    self.lines.append((self.start_pos, self.end_pos))
            if event.key == pygame.K_UP:
                self.drawing = not self.drawing
                if self.drawing:
                    self.lines.append((self.start_pos, (100, 100)))
