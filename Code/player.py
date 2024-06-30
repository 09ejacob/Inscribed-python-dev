import pygame
from utils import load_sprite_sheets

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height, player_id):
        super().__init__()
        print("Init player")
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.id = player_id  # Add player ID
        self.update_sprite()  # Ensure sprite is initialized

    @classmethod
    def from_dict(cls, data):
        """Initialize Player from dictionary."""
        player = cls(data['x'], data['y'], 50, 50, data['id'])
        player.x_vel = data['x_vel']
        player.y_vel = data['y_vel']
        player.direction = data['direction']
        player.animation_count = data['animation_count']
        player.update_sprite()  # Ensure sprite is initialized
        return player

    def update_from_dict(self, data):
        """Update Player from dictionary."""
        self.rect.x = data['x']
        self.rect.y = data['y']
        self.x_vel = data['x_vel']
        self.y_vel = data['y_vel']
        self.direction = data['direction']
        self.animation_count = data['animation_count']
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
            'id': self.id
        }

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
        if self.hit_count > fps * 2:
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
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
                print("Double jump")
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        #print("Animation count: ", self.animation_count)
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
