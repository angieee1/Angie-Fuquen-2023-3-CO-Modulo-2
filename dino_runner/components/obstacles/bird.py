import random
from dino_runner.components.obstacles.obstacle import Obstacle

from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, image):
        super().__init__(image, obstacle_type="bird")
        self.rect.y = random.randint(150, 300)
        self.step = 0

    def update(self, game_speed, obstacles):
        self.image = BIRD[0] if self.step <= 4 else BIRD[1]
        super().update(game_speed, obstacles)

        self.step_index +=1
        if self.step_index == 8:
            self.step_index = 0

       