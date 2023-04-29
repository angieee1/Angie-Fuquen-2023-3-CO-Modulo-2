import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self):
        obstacle = Cactus(SMALL_CACTUS)

        return obstacle

    def update(self,  game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle()
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

