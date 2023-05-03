import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_HEIGHT


class PowerUp(Sprite):
    def __init__(self, image, type):
        self.iamge = image
        self.type = type
        self.rect =self.image.get_rect()
        self.rect.x = SCREEN_HEIGHT
        self.rect.y = random.randint(120, 180)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        