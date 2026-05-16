import pygame
from const import SCREEN, screen_scale, get_font, button_height, button_width, update_scale, change_screen

def update_scale():
    for property in screen_scale:
        property = screen_scale[property]
    return screen_scale

def change_screen(width=1500, height=750, mode='windowed'):
    if mode == 'fullscreen':
        SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        current_screen_mode='Fullscreen'
        return SCREEN, current_screen_mode
    else:
        SCREEN = pygame.display.set_mode((width, height))
        current_screen_mode='Windowed'
        return SCREEN, current_screen_mode
    


class NavBar():
    def __init__(self, items, position):
        pass

class Popup():
    def __init__(self, label, close_button=True):
        pass

class TabMenu():
    pass

class GridMenu():
    pass