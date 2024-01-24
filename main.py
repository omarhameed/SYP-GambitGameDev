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
pg.display.set_caption("GAMBiT: Flicker Demo")

# Init the clock (sets the framerate)
clock = pg.time.Clock()

# Play music (not really necessary)
pg.mixer.music.load("music/shell.mp3")
pg.mixer.music.play(-1)

# Print the title
font = pg.font.Font(None, 64)
text = font.render("GAMBiT: Flicker Demo", True, "white")
textpos = text.get_rect(centerx = screen.get_width() / 2, y=10)
screen.blit(text, textpos)

# Super basic way to draw a square (target) at a given location
target_1 = Target(screen, 127, 127, 20, -1)
target_2 = Target(screen, 255, 511, 2, -1)

while True:
    for event in pg.event.get():

        # Handles the event where the user presses the Windows 'X'
        if event.type == pg.QUIT: 
            pg.quit()
            sys.exit()

    screen.fill("black")

    target_1.draw()
    target_2.draw()
    screen.blit(text, textpos)

    pg.display.flip()

    # Limit the framerate to the integer specified
    clock.tick(144)
