import pygame
from spellTableLineDrawer import SpellTableLineDrawer
from fireball import Fireball

class Spell:

    def __init__(self, line_drawer):
        self.spell_fireball = ["DOWN", "RIGHT", "UP"]
        self.spell_wall = ["LEFT", "DOWN", "RIGHT", "RIGHT", "UP", "LEFT"]
        self.line_drawer = line_drawer

    def detectSpell(self): # Add return here
        moves = self.line_drawer.getMoves()

        detected_spell = ""

        if moves == self.spell_fireball:
            #print("Fireball casted")
            detected_spell = "Fireball"
        elif moves == self.spell_wall:
            #print("Wall casted")
            detected_spell = "Wall"

        else:
            #print("No spell casted")
            detected_spell = "No spell"

        self.line_drawer.clearMovesAndLines()

        return detected_spell
