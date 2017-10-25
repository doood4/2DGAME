from pico2d import *

class Footman:
    def __init__(self):
        self.x, self.y = 0, 90
        self.xframe = 2
        self.yframe = 0
        self.image = load_image('Images\\human_footman.png')
        self.vector = (1,0)

    def update(self):
        if self.vector == (0,1):
            self.xframe = 0
        elif self.vector == (1,1):
            self.xframe = 1
        elif self.vector == (1,0):
            self.xframe = 2
        elif self.vector == (1,-1):
            self.xframe = 3
        elif self.vector == (0,-1):
            self.xframe = 4
        elif self.vector == (-1,-1):
            self.xframe = 5
        elif self.vector == (-1,0):
            self.xframe = 6
        elif self.vector == (-1,1):
            self.xframe = 7

        self.yframe = (self.yframe + 1) % 4
        self.x += self.vector[0] * 2
        self.y += self.vector[1] * 2
        if self.x >= 50:
            self.vector = (1,1)

    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50, self.x, self.y,40,40)


class Knight:
    def __init__(self):
        self.x, self.y = 0, 90
        self.xframe = 2
        self.yframe = 0
        self.image = load_image('Images\\human_knight.png')
        self.vector = (1,0)

    def update(self):
        if self.vector == (0,1):
            self.xframe = 0
        elif self.vector == (1,1):
            self.xframe = 1
        elif self.vector == (1,0):
            self.xframe = 2
        elif self.vector == (1,-1):
            self.xframe = 3
        elif self.vector == (0,-1):
            self.xframe = 4
        elif self.vector == (-1,-1):
            self.xframe = 5
        elif self.vector == (-1,0):
            self.xframe = 6
        elif self.vector == (-1,1):
            self.xframe = 7

        self.yframe = (self.yframe + 1) % 4
        self.x += self.vector[0] * 3
        self.y += self.vector[1] * 3
        if self.x >= 50:
            self.vector = (1,1)
        if self.y >= 300:
            self.vector = (0,1)

    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50, self.x, self.y,60,60)