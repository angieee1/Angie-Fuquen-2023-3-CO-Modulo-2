import pygame


from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

BLACK_COLOR  = (0,0,0)


def get_centered_message(message):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 +70)
    return text, text_rect

def get_centered_message_a(message):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 +105)
    return text, text_rect

def get_centered_message_b(message):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 +140)
    return text, text_rect
