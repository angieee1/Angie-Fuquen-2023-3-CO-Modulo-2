import random
import pygame
from dino_runner.components.power_ups.hammer import Hammer

from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self): #lista de power ups indica si hay uno generado actualmente y dos si va a generar más
        self.power_ups = []
        self.when_appears = random.randint (100, 200)
        self.duration = random.randint(3,5) #cuanto va a durar

    def generate_power_up(self): ## aqui se hace if para hacer el otro power up
        power_up = random.choice([Shield(), Hammer()])
        self.when_appears += random.randint(100, 200)
        self.power_ups.append(power_up) #se añade a la lista de power ups

    def update(self, game):
        if len(self. power_ups) == 0 and self.when_appears == game.score.count:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type
                game.player.has_power_up = True 
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)  #ver cuando termina
                self.power_ups.remove(power_up) # remueve el power de la pantalla porque ya se acabo el tiempo de uso


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = [] #se encarga de limpiar la lista 
        self.when_appears = random.randint(100, 200)
