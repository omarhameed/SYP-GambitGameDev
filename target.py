import pygame as pg

pg.init()
position_change_interval = 5  # determines number of seconds to change the target selector 

class Target:
    # Class attributes.
    timer = 0
    size = 64
    

    # Constructor function.
    def __init__(self, screen):
        # Instance attributes.
        self.screen = screen
  
   # Draw target statically.
    def draw(self, x_pos, y_pos, color):
        pg.draw.rect(self.screen, color, (x_pos, y_pos, self.size, self.size))

    
    # Flicker target.
    def flicker(self, rate, x_pos, y_pos, color):
        if self.timer >= rate:
            self.draw(x_pos, y_pos, color)
            self.timer = 0
        else:
            self.timer +=1

