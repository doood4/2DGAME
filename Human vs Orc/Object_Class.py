from pico2d import *

class Card:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.xsize = 70
        self.ysize = 100
        self.frame = 0

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 70, 100,
                             self.x, self.y,self.size,self.size)

