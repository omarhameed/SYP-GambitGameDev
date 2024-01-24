import pygame as pg

pg.init()

class Target:
    # Class attributes.
    timer = 0

    # Constructor function.
    def __init__(self, screen, x_pos, y_pos, size, freq):
        # Instance attributes.
        self.screen = screen
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
        self.freq = freq
  
    # Draw target statically.
    def draw(self):
        pg.draw.rect(self.screen, "white", (self.x_pos, self.y_pos, self.size, self.size))
    
    # Flicker target.
    def flicker(self):
        if self.timer >= self.freq:
            self.draw()
            self.timer = 0
        else:
            self.timer +=1
