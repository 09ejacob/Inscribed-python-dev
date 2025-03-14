import pygame
from object import Object
from utils import load_sprite_sheets

class SpellTable(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.spellTable = load_sprite_sheets("UI", "SpellTable", width, height)
        self.image = self.spellTable["Spell_Table-128"][0]