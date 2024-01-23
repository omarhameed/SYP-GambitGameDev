import pygame as pg

pg.init()

class Target:
    
    # Initialize target
    def __init__(self, screen, x_pos, y_pos, freq, focused):
        self.screen = screen
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.freq = freq
        self.focused = focused
  
    # Draw target on screen at predetermined position
    def draw(self):
        pg.draw.rect(self.screen, (255, 255, 255), (self.x_pos, self.y_pos, 64, 64))
