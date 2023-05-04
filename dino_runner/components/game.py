import pygame

from dino_runner.utils.constants import BG, BIRD, CLOUD, DEAD, DEFAULT_TYPE, ICON, IMAGE, LARGE_CACTUS, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.counter import Counter
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    GAME_SPEED = 20

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu(self.screen)
        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        self.power_up_manager = PowerUpManager()

    
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
        
    def run(self):
        
        self.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.score.update()
        self.update_game_speed()
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((199, 179, 255))
        self.draw_background()
        self.draw_clouds()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.draw_power_up_time()

        pygame.display.update()

    def draw_clouds(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +300, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +800, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +700, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +900, self.y_pos_bg -312))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +875, self.y_pos_bg -350))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +954, self.y_pos_bg -370))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2456, self.y_pos_bg -360))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +100, self.y_pos_bg -340))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +978, self.y_pos_bg -330))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1400, self.y_pos_bg -360))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +500, self.y_pos_bg -370))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +600, self.y_pos_bg -320))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1200, self.y_pos_bg -360))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +3573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +3573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1773, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +878, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1873, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1764, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2764, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2879, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +4573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +3573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +4573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +4573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +5573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +3573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2573, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2473, self.y_pos_bg -300))
        


    
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        self.menu.reset_screen_color(self.screen)

        if self.death_count.count == 0:
            self.menu.draw(self.screen, ' HII!! Press any key to start ...' , half_screen_width , half_screen_height - 10)
            self.screen.blit(DEAD, (SCREEN_WIDTH -140 , SCREEN_HEIGHT+0))

        else:
            self.update_highest_score()
            self.menu.draw(self.screen, 'Game over. Press any key to restart',half_screen_width , half_screen_height - 10 )
            self.menu.draw(self.screen, f'Your score: {self.score.count}', half_screen_width - 350, 350 )
            self.menu.draw(self.screen, f'Highest score: {self.highest_score.count}', half_screen_width, 350 )
            self.menu.draw(self.screen, f'Total deaths: {self.death_count.count}', half_screen_width + 350, 350 )
            
        
        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 150))
        self.screen.blit(CLOUD, (half_screen_width + 35, half_screen_height  + 120))
        self.screen.blit(CLOUD, (half_screen_width + 75, half_screen_height  -80))
        self.screen.blit(CLOUD, (half_screen_width + 30, half_screen_height  +60))
        self.screen.blit(CLOUD, (half_screen_width + 80, half_screen_height  -280))
        self.screen.blit(CLOUD, (half_screen_width - 400, half_screen_height  +240))
        self.screen.blit(CLOUD, (half_screen_width - 380, half_screen_height  -200))
        self.screen.blit(CLOUD, (half_screen_width + 340, half_screen_height  + 160))
        self.screen.blit(CLOUD, (half_screen_width - 340, half_screen_height  + 120))
        self.screen.blit(CLOUD, (half_screen_width + 300, half_screen_height  +80))
        self.screen.blit(CLOUD, (half_screen_width - 260, half_screen_height  -60))
        self.screen.blit(CLOUD, (half_screen_width + 220, half_screen_height  -280))
        self.screen.blit(CLOUD, (half_screen_width - 400, half_screen_height  +240))
        self.screen.blit(CLOUD, (half_screen_width - 350, half_screen_height  -200))
        self.screen.blit(CLOUD, (half_screen_width + 300, half_screen_height  + 160))
        self.screen.blit(CLOUD, (half_screen_width + 450, half_screen_height  -100))
        self.screen.blit(CLOUD, (half_screen_width - 550, half_screen_height  +80))
        self.screen.blit(CLOUD, (half_screen_width + 330, half_screen_height  -80))
        self.screen.blit(CLOUD, (half_screen_width - 500, half_screen_height  +80))
        self.screen.blit(CLOUD, (half_screen_width + 400, half_screen_height  -80))
        self.screen.blit(CLOUD, (half_screen_width - 250, half_screen_height  -80))
        self.screen.blit(CLOUD, (half_screen_width + 400, half_screen_height  + 80))
        self.screen.blit(CLOUD, (half_screen_width - 300, half_screen_height  -80))
        self.screen.blit(CLOUD, (half_screen_width + 300, half_screen_height  +80))
        self.screen.blit(BIRD[0], (half_screen_width+50 , half_screen_height-100))
        self.screen.blit(BIRD[0], (half_screen_width-170 , half_screen_height-100))
        self.screen.blit(BIRD[1], (half_screen_width-50 , half_screen_height-250))
        self.screen.blit(LARGE_CACTUS[2], (half_screen_width -240 , half_screen_height+0))
        self.screen.blit(LARGE_CACTUS[2], (half_screen_width +140 , half_screen_height+0))
        self.screen.blit(DEAD, (half_screen_width +465 , half_screen_height ))
        self.screen.blit(IMAGE, (half_screen_width -550 , half_screen_height ))
        self.screen.blit(DEAD, (half_screen_width +465 , half_screen_height + 150))
        self.screen.blit(IMAGE, (half_screen_width +380 , half_screen_height + 150))
        self.screen.blit(DEAD, (half_screen_width -465 , half_screen_height + 150))
        self.screen.blit(IMAGE, (half_screen_width -550 , half_screen_height + 150))
        
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        self.menu.update(self)
        
    def update_game_speed(self):
        if self.score.count % 100 == 0 and self.game_speed < 250:
            self.game_speed += 2
            
    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)

    def reset(self):
        self.obstacle_manager.reset()
        self.score.reset()
        self.game_speed = self.GAME_SPEED
        self.player.reset()
        self.power_up_manager.reset()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                self.menu.draw(self.screen, f'{self.player.type.capitalize()} enabled for {time_to_show} seconds', 540, 50)

            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
     
    