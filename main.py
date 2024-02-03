# GAMBIT Flicker Demo!
# Created by Connor McLeod for ECED 4502.

import sys
import pygame as pg
import random
import time 

from target import Target

pg.init()
last_position_change_time = 0
position_change_interval = 30  # determines number of seconds to change the target selector 

# Global variable to track if it's the first run
first_run = True

#  function returns the number of seconds passed since epoch, this is used to set an interval 
def current_time():
    return time.time()

 
   

    

# Function to dynamically determine how to arrange targets on screen.
def target_arrange(num_targets):
    x_pos = 0
    y_pos = 0 
    # Initialize the array to store x_pos values
    x_target = []
    y_target =[]
    global last_position_change_time, position_change_interval
    black_target_index = -1

    if num_targets != 9:
        y_pos = (DISPLAY.get_height() / 2)
        for i in range(num_targets):
            x_pos = (DISPLAY.get_width() / (num_targets + 1)) + x_pos
            
            # Store the x_pos value in the array
            x_target.append(x_pos)
            y_target.append(y_pos)
            targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "red")
            # Calculate the time passed since the last position change

            
            
            countdown = current_time() - last_position_change_time
            print(f"Countdown: {countdown}, Interval: {i}")  # Debugging line

            if countdown >= position_change_interval  :
                
                black_target_index = random.randint(0, num_targets - 1)  # Choose a new target to be black.
                last_position_change_time = current_time()  # Reset the last position change time to now
                position_change_interval = 5  # Reset the interval
                print(f"New black target is {black_target_index}")  # Print the new target for demonstration purposes
            else:
                pass
            if i == black_target_index : 
                print(f"New black target is {black_target_index}")  # Print the new target for demonstration purposes

                targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "green")
            else :
                targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "red")



    else: 
        # Code for arranging targets in a 3x3 grid
        grid_size = 3  # Because it's a 3x3 grid
        x_gap = DISPLAY.get_width() / (grid_size + 1)
        y_gap = DISPLAY.get_height() / (grid_size + 1)
        positions = [(x_gap * (i % grid_size + 1), y_gap * (i // grid_size + 1)) for i in range(num_targets)]

        for i, (x_pos, y_pos) in enumerate(positions):
            x_target.append(x_pos)  # Append x_pos instead of x_gap
            y_target.append(y_pos)  # Append y_pos instead of y_gap
            
            
            if i == black_target_index : 
                print("hit it")
                targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "green")
            else:
                targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "red")
            # Calculate the time passed since the last position change
            countdown = current_time() - last_position_change_time
            if countdown >= position_change_interval  :
                black_target_index = random.randint(0, num_targets - 1)  # Choose a new target to be black.
                last_position_change_time = current_time()  # Reset the last position change time to now
                position_change_interval = 5  # Reset the interval





    


# Initalizes the main display surface.
WIDTH = 2000
HEIGHT = 800
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

# Super basic way to draw a square (target) at a given location.
targets = []
for i in range(9):
    targets.append(Target(DISPLAY))

# Game state variable that tracks which portion of the game's execution we are in.
state = 0
timer_event = pg.USEREVENT + 1
pg.time.set_timer(timer_event, 3000)

# Game loop begins!
while True:
    for event in pg.event.get():
        # User exits the program.
        if event.type == pg.QUIT: 
            pg.quit()
            sys.exit()

        # Timer event that triggers every 3000 frames.
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
        target_arrange(1)


    # Begin Test 2.
    if state == 2:
        print(f"State: {state}")
        # Add code for Test 2!
        text = font.render("Test 2. Three targets will be shown flickering at differing frequencies.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)
        target_arrange(3)


    # Begin Test 3.
    if state == 3:
        print(f"State: {state}")
        # Add code for Test 3!
        text = font.render("Test 3. Four targets will be shown at each of the four corners of the display.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)
        target_arrange(4)

    # Begin Test 4.         
    if state == 4:
        print(f"State: {state}")
        # Add code for Test 4!
        text = font.render("Test 4. Nine targets will be shown in a 3x3 grid.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)
        target_arrange(9)

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
