import pygame


from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

BLACK_COLOR  = (0,0,0)
PURPLE = (120, 0, 255)

X = SCREEN_WIDTH
Y = SCREEN_HEIGHT


def draw__message(message):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, PURPLE)
    text_rect = text.get_rect()
    text_rect.center = (X // 2 , Y // 2 )
    return text, text_rect


