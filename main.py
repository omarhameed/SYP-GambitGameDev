# GAMBIT Flicker Demo!
# Created by Connor McLeod for ECED 4502.

import sys
import pygame as pg

from target import Target

pg.init()

# Initalizes the main display surface.
WIDTH = 1920
HEIGHT = 1080
DISPLAY = pg.display.set_mode((WIDTH, HEIGHT))

# Set the framerate (can be set higher if you have a high-framerate display).
FPS = 60
framerate = pg.time.Clock()

# Play music!
pg.mixer.music.load("music/menu.mp3")
pg.mixer.music.play(-1)

# Print the title
font = pg.font.Font(None, 32)
text = font.render("Welcome to the GAMBIT Flicker Demo! Please be aware there will be many flashing lights.", True, "black")
textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)

# Super basic way to draw a square (target) at a given location
target_1 = Target(DISPLAY, ((DISPLAY.get_width() / 2) - 256 / 2), ((DISPLAY.get_height() / 2) - 128), 256, 4)

# Game state variable that tracks which portion of the game's execution we are in.
state = 0
timer_event = pg.USEREVENT + 1
pg.time.set_timer(timer_event, 5000)

# Game loop begins!
while True:
    for event in pg.event.get():
        # User exits the program.
        if event.type == pg.QUIT: 
            pg.quit()
            sys.exit()

        # Timer event that triggers every 5000 frames.
        if event.type == timer_event:
            if state >= 5:
                state = 0
            else:
                state += 1

    # Clear the display.
    DISPLAY.fill("white")

    # Show title screen.
    if state == 0:
        print(f"State: {state}")
        # Add code for title screen!
        text = font.render("Welcome to the GAMBIT Flicker Demo! Please be aware there will be many flashing lights.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)
    
    # Begin Test 1.
    if state == 1:
        print(f"State: {state}")
        # Add code for Test 1!
        text = font.render("Test 1. A single flickering target will be shown.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)
        target_1.flicker()

    # Begin Test 2.
    if state == 2:
        print(f"State: {state}")
        # Add code for Test 2!
        text = font.render("Test 2. Three targets will be shown flickering at differing frequencies.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)

    # Begin Test 3.
    if state == 3:
        print(f"State: {state}")
        # Add code for Test 3!
        text = font.render("Test 3. Four targets will be shown at each of the four corners of the display.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)

    # Begin Test 4.         
    if state == 4:
        print(f"State: {state}")
        # Add code for Test 4!
        text = font.render("Test 4. Nine targets will be shown in a 9x9 grid.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)

    # Congratulate the user!
    if state == 5:
        print(f"State: {state}")
        # Add code!
        text = font.render("Thank you for taking part in our experiment!", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)

    DISPLAY.blit(text, textpos)

    pg.display.update()

    # Limit the framerate to the integer specified
    framerate.tick(FPS)
