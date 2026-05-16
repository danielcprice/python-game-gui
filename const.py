import pygame

pygame.font.init()

SCREEN = pygame.display.set_mode((1500, 750))
current_screen_mode='Windowed'
screen_scale = {'screen_height': SCREEN.get_height(), 'screen_width': SCREEN.get_width(), 'button_height': (SCREEN.get_height() * .1), 'button_width': (SCREEN.get_width() * .15), 'center_x': ((SCREEN.get_width() / 2) - ((SCREEN.get_width() * .15) / 2)), 'center_y': ((SCREEN.get_height() / 2) - ((SCREEN.get_height() * .1) / 2))}

button_height = SCREEN.get_height() * .1
button_width = SCREEN.get_width() * .15

def get_font(size=30):
    font = pygame.font.Font('./assets/pixeloid.sans-bold.ttf', size)
    return font
