import pygame
from os import listdir
from os.path import isfile, join
from network import Network

pygame.init()
pygame.display.set_caption("Inscribed")

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

player_id = Network().id
previous_id = 0

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites] # True for flip in x direction. False for flip in y direction

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))] # Load every file inside the directory

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface)) # scale2x makes the sprites (which are 32px) to 64px.

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites

def get_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size) # Need to change the 96 and 0 and the size when wanting to load a different terrain/block
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_background(name, width, height):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, img_width, img_height = image.get_rect() # Ignoring the x and y
    tiles = []

    for i in range(width // img_width + 1):
        for j in range(height // img_height + 1):
            pos = (i * img_width, j * img_height)
            tiles.append(pos)

    return tiles, image

def assign_skin():
    if player_id % 2 == 0:
        skin = "MaskDude"
        print("MaskDude selected and count set to: ", player_id)
    else:
        skin = "NinjaFrog"
        print("NinjaFrog selected and count set to: ", player_id)

    return skin