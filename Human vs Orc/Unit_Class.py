from pico2d import *
from main_state import *


#############  HUMAN  ###############
class Peasant:

    image = None

    def __init__(self):
        self.x, self.y = 150, 130
        self.size = 40
        self.xframe = 2
        self.yframe = 0
        self.vector = (-1,-1)

        if Peasant.image == None:
            Peasant.image = self.image = load_image('Images\\human_peasant.png')

    def update(self):
        if self.vector == (-1,-1):
            self.xframe = 0
        elif self.vector == (1,1):
            self.xframe = 1

        self.yframe = (self.yframe + 1) % 4
        self.x += self.vector[0] * 2
        self.y += self.vector[1] * 2
        if self.y < 30:
            self.vector = (1,1)
            self.y = 60
        elif self.x > 150:
            self.vector = (-1,-1)
            self.y = 130
            
    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50,
                             self.x, self.y,self.size,self.size)


class Footman:
    image = None

    def __init__(self):
        self.x, self.y = 0, 90
        self.size = 40
        self.xframe = 2
        self.yframe = 0
        self.vector = (1, 0)

        if Footman.image == None:
            Footman.image = self.image = load_image('Images\\human_footman.png')

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
        self.x += self.vector[0] * 1
        self.y += self.vector[1] * 1
        if self.x >= 50:
            self.vector = (1,1)

    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50,
                             self.x, self.y,self.size,self.size)


class Archer:
    image = None

    def __init__(self):
        self.x, self.y = 0, 90
        self.size = 40
        self.xframe = 2
        self.yframe = 0
        self.vector = (1, 0)

        if Footman.image == None:
            Footman.image = self.image = load_image('Images\\human_archer.png')

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
        self.x += self.vector[0] * 1
        self.y += self.vector[1] * 1
        if self.x >= 50:
            self.vector = (1,1)

    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50,
                             self.x, self.y,self.size,self.size)


class Mage:
    image = None

    def __init__(self):
        self.x, self.y = 0, 90
        self.size = 40
        self.xframe = 2
        self.yframe = 0
        self.vector = (1, 0)

        if Footman.image == None:
            Footman.image = self.image = load_image('Images\\human_mage.png')

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
        self.x += self.vector[0] * 1
        self.y += self.vector[1] * 1
        if self.x >= 50:
            self.vector = (1,1)

    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50,
                             self.x, self.y,self.size,self.size)


class Knight:
    image = None

    def __init__(self):
        self.x, self.y = 0, 90
        self.size = 60
        self.xframe = 2
        self.yframe = 0
        self.vector = (1, 0)
        if Knight.image == None:
            Knight.image = load_image('Images\\human_knight.png')

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
        if self.y >= 300:
            self.vector = (0,1)

    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50,
                             self.x, self.y,self.size,self.size)