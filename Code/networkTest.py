import pygame

class networkTest(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, test_id):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.speed = 1
        self.id = test_id


    @classmethod
    def from_dict(cls, data):
        test = cls(data['x'], data['y'], 50, 50, data['id'])
        test.x_vel = data.get('x_vel', 0)
        test.y_vel = data.get('y_vel', 0)
        return test

    def update_from_dict(self, data):
        self.rect.x = data.get('x', self.rect.x)
        self.rect.y = data.get('y', self.rect.y)
        self.x_vel = data.get('x_vel', self.x_vel)
        self.y_vel = data.get('y_vel', self.y_vel)

    def to_dict(self):
        return {
            'x': self.rect.x,
            'y': self.rect.y,
            'x_vel': self.x_vel,
            'y_vel': self.y_vel,
            'id': self.id,
        }
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel

    def move_right(self, vel):
        self.x_vel = vel

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
