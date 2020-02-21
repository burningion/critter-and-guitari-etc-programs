"""
Draw a restless circle.

* Use with Auto Clear Toggle Off
Knob 1: Circle restlessness (position randomness)
Knob 2: Max circle size
Knob 3: Circle fade
Knob 4: Circle color
Knob 5: Background color
"""
import os
import pygame
import random


def setup(screen, etc):
    pass

def draw(screen, etc):
    size = int(etc.knob2 * 360)
    x = int(640 + (random.random() - 0.5) * 1280 * etc.knob1)
    y = int(360 + (random.random() - 0.5) * 720 * etc.knob1)
    color = etc.color_picker()
    pygame.draw.circle(screen, color, (x, y), size)

    #TRAILS
    veil = pygame.Surface((1280, 720))
    veil.set_alpha(int(etc.knob3 * 200)) # adjust transparency on knob3
    bg_color = etc.color_picker_bg()
    veil.fill((bg_color[0], bg_color[1], bg_color[2]))
    screen.blit(veil, (0, 0)) # (0,0) = starts at top left
