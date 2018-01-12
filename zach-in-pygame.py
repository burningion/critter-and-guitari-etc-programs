import pygame
import random
import time
import math

# original code adapted from zach lieberman's talk
# https://www.youtube.com/watch?v=bmztlO9_Wvo

def setup(screen, etc):
    pass

def draw(screen, etc):
    for i in range(720):
        color = (int(127 + 127 * math.sin(i * .01 + time.time())),
                 int(127 + 127 * math.sin(i * .011 + time.time())),
                 int(127 + 127 * math.sin(i * .012 + time.time())))
        radius = int(50 + 40 * math.sin(i * .005 + time.time()))
        xpos = int(1280 // 2 + 100 * math.sin(i * .02 + time.time()))
        pygame.gfxdraw.filled_circle(screen, xpos, i, radius, color)
