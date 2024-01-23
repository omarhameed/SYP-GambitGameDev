# GamBit Flicker Demo
# Created by Connor McLeod

import sys
import pygame as pg

from target import Target

# Starts pygame
pg.init()

# Init the screen to a pre-determined size
size = width, height = 1920, 1080
screen = pg.display.set_mode(size)

# Set the window caption
pg.display.set_caption("GamBit Flicker Demo")

# Init the clock (sets the framerate)
clock = pg.time.Clock()

# Play music (not really necessary)
pg.mixer.music.load("music/shell.mp3")
pg.mixer.music.play(-1)

# Super basic way to draw a square (target) at a given location
target_1 = Target(screen, 127, 127, -1, -1)
target_1.draw()

target_2 = Target(screen, 255, 511, -1, -1)
target_2.draw()

while True:
    for event in pg.event.get():

        # Handles the event where the user presses the Windows 'X'
        if event.type == pg.QUIT: 
            pg.quit()
            sys.exit()

    pg.display.update()

    # Limit the framerate to the integer specified
    clock.tick(144)
