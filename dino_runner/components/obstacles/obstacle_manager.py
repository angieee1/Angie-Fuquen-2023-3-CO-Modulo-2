import pygame
import random
from dino_runner.components.obstacles.bird import Bird

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, SMALL_CACTUS, LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self, typex):
        if typex == 0:
            obstacle = Bird(BIRD[0])
            
        elif typex == 1:
          obstacle = Cactus(SMALL_CACTUS)  ## esta forma abstrae el funcionamiento de crear el obstaculo
        elif typex == 2:
            obstacle = Cactus(LARGE_CACTUS)

        return obstacle

    def update(self, game):
        if len(self.obstacles) == 0:
            typex = random.randint(0,2)

            obstacle = self.generate_obstacle(typex)
            self.obstacles.append(obstacle) ##append añade elemento nuevo a la lista final.

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing=False
                pygame.time.delay(500)
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

