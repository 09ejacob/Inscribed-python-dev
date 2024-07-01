import pygame
from object import Object
from utils import load_sprite_sheets

class SpellTable(Object):
    current_line_pos = [0, 0]

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.spellTable = load_sprite_sheets("UI", "SpellTable", width, height)
        self.image = self.spellTable["Spell_Table-128"][0]

    def draw_line(self, window):
        pygame.draw.line(window, (255,0,0), (0,0), (500,500), 5)
        pygame.display.flip()