from pico2d import *
import main_state



#############  HUMAN  ###############

class Peasant:

    image = None
    plus10 = None

    def __init__(self):
        self.cost = 50
        self.x, self.y = 350, 15
        self.speed = 10
        self.size = 30
        self.xframe = 2
        self.yframe = 0
        self.vector = (1,0)
        main_state.Gold -= self.cost

        if Peasant.image == None:
            Peasant.image = self.image = load_image('Images\\human_peasant.png')
        if Peasant.plus10 == None:
            Peasant.plus10 = self.plus10 = load_image('plus10.png')

    def update(self):
        if self.vector == (1,0):
            self.xframe = 0
        elif self.vector == (-1,0):
            self.xframe = 1

        self.yframe = (self.yframe + 1) % 4
        self.x += self.vector[0] * self.speed
        self.y += self.vector[1] * self.speed
        if self.x > 510:
            self.vector = (-1,0)
            self.y += 30
        elif self.x < 350:
            self.vector = (1,0)
            self.y -= 30


    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50,
                             self.x, self.y,self.size,self.size)
        if self.y == 45 and self.x == 350:
            self.plus10.draw(self.x, self.y + 50)
            main_state.Gold += 10


class Footman:
    image = None

    def __init__(self):
        self.cost = 50
        self.x, self.y = main_state.mx, main_state.my
        self.size = 40
        self.xframe = 2
        self.yframe = 0
        self.vector = (0, 1)

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


    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50,
                             self.x, self.y,self.size,self.size)


class Archer:
    image = None

    def __init__(self):
        self.cost = 50
        self.x, self.y = main_state.mx, main_state.my
        self.size = 40
        self.xframe = 2
        self.yframe = 0
        self.vector = (0, 1)

        if Archer.image == None:
            Archer.image = self.image = load_image('Images\\human_archer.png')

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


    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50,
                             self.x, self.y,self.size,self.size)


class Knight:
    image = None

    def __init__(self):
        self.cost = 50
        self.x, self.y = main_state.mx, main_state.my
        self.size = 60
        self.xframe = 2
        self.yframe = 0
        self.vector = (0, 1)
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


    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50,
                             self.x, self.y,self.size,self.size)


class Mage:
    image = None

    def __init__(self):
        self.cost = 50
        self.x, self.y = main_state.mx, main_state.my
        self.size = 40
        self.xframe = 2
        self.yframe = 0
        self.vector = (0, 1)

        if Mage.image == None:
            Mage.image = self.image = load_image('Images\\human_mage.png')

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


    def draw(self):
        self.image.clip_draw(self.xframe * 50, self.yframe * 50, 50, 50,
                             self.x, self.y,self.size,self.size)