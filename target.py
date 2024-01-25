import pygame as pg

pg.init()

class Target:
    # Class attributes.
    timer = 0
    size = 64

    # Constructor function.
    def __init__(self, screen):
        # Instance attributes.
        self.screen = screen
  
    # Draw target statically.
    def draw(self, x_pos, y_pos):
        pg.draw.rect(self.screen, "red", (x_pos, y_pos, self.size, self.size))
    
    # Flicker target.
    def flicker(self, rate, x_pos, y_pos):
        if self.timer >= rate:
            self.draw(x_pos, y_pos)
            self.timer = 0
        else:
            self.timer +=1
