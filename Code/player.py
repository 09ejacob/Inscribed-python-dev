import pygame
from utils import load_sprite_sheets

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = {
        "MaskDude": load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True),
        "NinjaFrog": load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)
    }
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height, player_id, skin="MaskDude"):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.sprite_sheet = "idle"
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.id = player_id  # Add player ID
        self.skin = skin  # Add skin
        self.x_pos = x
        self.y_pos = y
        self.update_sprite()  # Ensure sprite is initialized

    @classmethod
    def from_dict(cls, data):
        """Initialize Player from dictionary."""
        player = cls(data['x'], data['y'], 50, 50, data['id'], skin=data.get('skin', 'MaskDude'))
        player.x_vel = data.get('x_vel', 0)
        player.y_vel = data.get('y_vel', 0)
        player.direction = data.get('direction', 'left')
        player.animation_count = data.get('animation_count', 0)
        player.sprite_sheet = data.get('sprite_sheet', 'idle')
        player.hit_count = data.get('hit_count', 0)
        player.hit = data.get('hit', False)
        player.update_sprite()  # Ensure sprite is initialized
        return player

    def update_from_dict(self, data):
        """Update Player from dictionary."""
        self.rect.x = data.get('x', self.rect.x)
        self.rect.y = data.get('y', self.rect.y)
        self.x_vel = data.get('x_vel', self.x_vel)
        self.y_vel = data.get('y_vel', self.y_vel)
        self.direction = data.get('direction', self.direction)
        self.animation_count = data.get('animation_count', self.animation_count)
        self.sprite_sheet = data.get('sprite_sheet', self.sprite_sheet)
        self.hit_count = data.get('hit_count', self.hit_count)
        self.hit = data.get('hit', self.hit)
        self.skin = data.get('skin', self.skin)  # Update skin
        self.update_sprite()

    def to_dict(self):
        """Convert Player to dictionary."""
        return {
            'x': self.rect.x,
            'y': self.rect.y,
            'x_vel': self.x_vel,
            'y_vel': self.y_vel,
            'direction': self.direction,
            'animation_count': self.animation_count,
            'sprite_sheet': self.sprite_sheet,
            'hit_count': self.hit_count,
            'hit': self.hit,
            'id': self.id,
            'skin': self.skin  # Add skin to dictionary
        }

    def get_x_pos(self):
        return self.x_pos
    
    def get_y_pos(self):
        return self.y_pos

    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True
        self.hit_count = 0

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 1:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.update_sprite()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        if self.hit:
            self.sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                self.sprite_sheet = "jump"
            elif self.jump_count == 2:
                self.sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            self.sprite_sheet = "fall"
        elif self.x_vel != 0:
            self.sprite_sheet = "run"
        else:
            self.sprite_sheet = "idle"
            if self.animation_count > 1000:
                self.animation_count = 0

        sprite_sheet_name = self.sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[self.skin][sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1

        #print("Sprite sheet: ", self.sprite_sheet, "Animation_count: ", self.animation_count)
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
