import pygame

import random
import math

# squares is square width in pixels
squares = 80
lines = []

def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def rotateLinePoints(start, end, degrees):
    startx, starty = start
    endx, endy = end

    middleX = (startx + endx) // 2
    middleY = (starty + endy) // 2
    inRadians = math.radians(degrees)
    newStart = rotate((middleX, middleY), start, inRadians)
    newEnd = rotate((middleX, middleY), end, inRadians)
    
    return newStart, newEnd

def generate_lines(squares):
    lines = []
    for x in range(0, 1280, squares):
        for y in range(0, 720, squares):
            if random.random() > 0.5:           
                lines.append([x, y, x + squares, y + squares])  
            else:
                lines.append([x, y + squares, x + squares, y])
    return lines

def setup(screen, etc):
    global lines
    lines = generate_lines(squares)

def draw(screen, etc):
    global lines, squares
    color = etc.color_picker()
    thickness = int(1 + etc.knob1 * 20)
    squares = int(50 + 50 * etc.knob3)
    
    if etc.audio_trig:
        lines = generate_lines(squares)
        for line in lines:
            l1, l2 = line[2:], line[:2]
            pygame.draw.line(screen, color, l1, l2, thickness)
    else:
        for p, line in enumerate(lines):
            l1, l2 = rotateLinePoints(line[:2], line[2:], etc.audio_in[p % 100] * .01 * etc.knob2)
            pygame.draw.line(screen, color, l1, l2, thickness)
    