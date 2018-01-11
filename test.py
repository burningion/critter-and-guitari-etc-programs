import pygame

def setup(screen, etc):
    pass

def draw(screen, etc):
    pygame.gfxdraw.filled_circle(screen, 
                                 1280 // 2,
                                 720 // 2,
                                 50, 
                                 (128, 254, 3))