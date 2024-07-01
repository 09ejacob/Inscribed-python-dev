import pygame

class SpellTableLineDrawer:
    def __init__(self):
        self.lines = []  # List to store lines drawn by the local player
        self.drawing = False
        self.start_pos = (100, 100)
        self.end_pos = (500, 500)

    def draw(self, window):
        # Draw lines
        for line in self.lines:
            pygame.draw.line(window, (255, 0, 0), line[0], line[1], 5)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.drawing = not self.drawing
                if self.drawing:
                    self.lines.append((self.start_pos, self.end_pos))
