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

    def draw_x(self, x_pos, y_pos):
        # Calculate the end points of the first line (top-left to bottom-right)
        start_pos1 = (x_pos, y_pos)
        end_pos1 = (x_pos + self.size, y_pos + self.size)
        
        # Calculate the end points of the second line (bottom-left to top-right)
        start_pos2 = (x_pos, y_pos + self.size)
        end_pos2 = (x_pos + self.size, y_pos)
        
        # Draw the first line
        pg.draw.line(self.screen, "black", start_pos1, end_pos1, width=2)
        
        # Draw the second line
        pg.draw.line(self.screen, "black", start_pos2, end_pos2, width=2)
    
    # Flicker target.
    def flicker(self, rate, x_pos, y_pos):
        if self.timer >= rate:
            self.draw(x_pos, y_pos)
            self.timer = 0
        else:
            self.timer +=1
