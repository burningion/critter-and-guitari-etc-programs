import pygame
import pygame.gfxdraw

# used to import a file name from the command line
import importlib
import argparse

import os

parser = argparse.ArgumentParser(description="Critter and Guitari ETC program debug environment")
parser.add_argument('module', type=str, help="Filename of the Pygame program to test")
parser.add_argument('-r', '--record', type=int, help="Record out to image sequence for ffmpeg")
args = parser.parse_args()

# imports the actual module we're loading
etc_mode = importlib.import_module(args.module.split('.py')[0])

import random
import math

from pygame.color import THECOLORS

# initialize to ETC's resolution
screenWidth, screenHeight = 1280, 720
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Knob values and settings
knobs = {1: 0.5, 2: 0.5, 3: 0.5, 4: 0.2, 5: 0.5, "step": 0.01}

# give ourselves some initial values
class ETC(object):
    def __init__(self):
        for knob_id in range(1, 6):
            setattr(self, f"knob{knob_id}", knobs[knob_id])

        self.audio_in = [random.randint(-32768, 32767) for i in range(100)]
        self.bg_color = (0, 0, 0)
        self.audio_trig = False
        self.midi_note_new = False
        self.mode_root = os.path.dirname(etc_mode.__file__)

    def color_picker(self):
        """
        Original color_picker function from ETC. See link below:
        https://github.com/critterandguitari/ETC_Mother/blob/master/etc_system.py
        """
        # convert knob to 0-1
        c = float(self.knob4)

        # all the way down random bw
        rando = random.randrange(0, 2)
        color = (rando * 255, rando * 255, rando * 255)

        # random greys
        if c > .02 :
            rando = random.randrange(0,255)
            color = (rando, rando, rando)
        # grey 1
        if c > .04 :
            color = (50, 50, 50)
        # grey 2
        if c > .06 :
            color = (100, 100 ,100)
        # grey 3
        if c > .08 :
            color = (150, 150 ,150)
        # grey 4
        if c > .10 :
            color = (150, 150 ,150)

        # grey 5
        if c > .12 :
            color = (200, 200 ,200)
        # white
        if c > .14 :
            color = (250, 250 ,250)
        #colors
        if c > .16 :
            r = math.sin(c * 2 * math.pi) * .5 + .5
            g = math.sin(c * 4 * math.pi) * .5 + .5
            b = math.sin(c * 8 * math.pi) * .5 + .5
            color = (r * 255,g * 255,b * 255)
        # full ranoms
        if c > .96 :
            color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        # primary randoms
        if c > .98 :
            r = random.randrange(0, 2) * 255
            g = random.randrange(0, 2) * 255
            b = random.randrange(0, 2) * 255
            color = (r,g,b)

        color2 = (color[0], color[1], color[2])
        return color2

    def color_picker_bg(self):
        """
        Original color_picker_bg function from ETC. See link below:
        https://github.com/critterandguitari/ETC_Mother/blob/master/etc_system.py
        """
        c = self.knob5
        r = (1 - (math.cos(c * 3 * math.pi) * .5 + .5)) * c
        g = (1 - (math.cos(c * 7 * math.pi) * .5 + .5)) * c
        b = (1 - (math.cos(c * 11 * math.pi) * .5 + .5)) * c

        color = (r * 255,g * 255,b * 255)

        self.bg_color = color
        return color


def update_knobs(key, knobs):
    """Update knobs but pressing a number between 1 - 4 and up/down keys together"""
    for knob_id in range(1, 6):
        if key[getattr(pygame, f"K_{knob_id}")] and key[pygame.K_UP]:
            knobs[knob_id] += knobs["step"]
            knobs[knob_id] = min(knobs[knob_id], 1.0)
            setattr(etc, f"knob{knob_id}", knobs[knob_id])
        if key[getattr(pygame, f"K_{knob_id}")] and key[pygame.K_DOWN]:
            knobs[knob_id] -= knobs["step"]
            knobs[knob_id] = max(knobs[knob_id], 0.0)
            setattr(etc, f"knob{knob_id}", knobs[knob_id])

etc = ETC()

etc_mode.setup(screen, etc)

running = True

recording = False
counter = -1

if args.record:
    recording = True

if recording:
    if not os.path.exists('imageseq'):
        os.makedirs('imageseq')
    counter = 0

while running:
    screen.fill(THECOLORS['black'])
    etc_mode.draw(screen, etc)

    key = pygame.key.get_pressed()
    update_knobs(key, knobs)
    if key[pygame.K_q]:
        exit()
    if key[pygame.K_SPACE]:
        etc.audio_trig = True
    if key[pygame.K_z]:
        etc.audio_trig = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if you try to quit, let's leave this loop
            running = False
    pygame.display.flip()

    if recording and counter < args.record:
        pygame.image.save(screen, "imageseq/%05d.jpg" % counter)
        counter += 1
    elif recording and counter == args.record:
        exit()
