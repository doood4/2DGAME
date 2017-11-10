from pico2d import *
import main_state



#############  HUMAN  ###############

class Peasant:

    image = None
    plus10 = None

    PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
    RUN_SPEED_KMPH = 10.0  # Km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.x, self.y = 350, 15
        self.size = 30
        self.state = 2
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.vector = (1,0)
        main_state.Gold -= 50

        if Peasant.image == None:
            Peasant.image = self.image = load_image('Images\\human_peasant.png')
        if Peasant.plus10 == None:
            Peasant.plus10 = self.plus10 = load_image('plus10.png')

    def update(self,frame_time):
        if self.vector == (1,0):
            self.state = 0
        elif self.vector == (-1,0):
            self.state = 1

        self.life_time += frame_time
        distance = Peasant.RUN_SPEED_PPS * frame_time
        self.total_frames += Peasant.FRAMES_PER_ACTION * Peasant.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        self.x += self.vector[0] * distance
        self.y += self.vector[1] * distance

        if self.x > 510:
            self.vector = (-1,0)
            self.y += 30
        elif self.x < 350:
            self.vector = (1,0)
            self.y -= 30

    def draw(self):
        self.image.clip_draw(self.state * 50, self.frame * 50, 50, 50,
                             self.x, self.y,self.size,self.size)
        if self.x < 350:
            self.plus10.draw(self.x, self.y + 50)
            main_state.Gold += 10

class Footman:
    image = None
    life_box = None

    PIXEL_PER_METER = (10.0 / 0.5)                     # 10 pixel 50 cm
    RUN_SPEED_KMPH = 4.0                               # Km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.x, self.y = main_state.mx, main_state.my
        self.size = 50
        self.state = 2
        self.frame = 0
        self.motion = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.vector = (0, 1)

        self.hp = 15
        self.atk = 0.1

        if Footman.image == None:
            Footman.image = load_image('Images\\human_footman.png')
        if Footman.life_box == None:
            Footman.life_box = load_image('Images\\life.png')


    def update(self,frame_time):
        if self.hp < 0 :
            main_state.unitList.remove(self)

        if self.vector == (0,1):
            self.state = 0
        elif self.vector == (1,1):
            self.state = 1
        elif self.vector == (1,0):
            self.state = 2
        elif self.vector == (1,-1):
            self.state = 3
        elif self.vector == (0,-1):
            self.state = 4
        elif self.vector == (-1,-1):
            self.state = 5
        elif self.vector == (-1,0):
            self.state = 6
        elif self.vector == (-1,1):
            self.state = 7

        for enemy in main_state.enemyList:
            if main_state.collide(enemy, self):
                self.motion = 4
                if self.frame == 4:
                    enemy.hp -= self.atk
            else:
                self.motion = 0


        self.life_time += frame_time
        distance = Footman.RUN_SPEED_PPS * frame_time
        self.total_frames += Footman.FRAMES_PER_ACTION * Footman.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4 + self.motion
        if self.motion == 4:
            distance = 0
        else:
            self.x += self.vector[0] * distance
            self.y += self.vector[1] * distance

    def draw(self):
        self.image.clip_draw(self.state * 50, self.frame * 50, 50, 50,
                             self.x, self.y,self.size,self.size)
        for i in range(int(self.hp)):
            self.life_box.draw(self.x - 15 + i*2, self.y - 20,2,4)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    #사거리
    def get_rb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_rb(self):
        draw_rectangle(*self.get_rb())


class Archer:
    image = None
    life_box = None

    PIXEL_PER_METER = (10.0 / 0.5)                     # 10 pixel 50 cm
    RUN_SPEED_KMPH = 4.0                               # Km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.x, self.y = main_state.mx, main_state.my
        self.size = 50
        self.state = 2
        self.frame = 0
        self.motion = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.vector = (0, 1)

        self.hp = 10
        self.atk = 0.1

        if Archer.image == None:
            Archer.image = self.image = load_image('Images\\human_archer.png')
        if Archer.life_box == None:
            Archer.life_box = load_image('Images\\life.png')

    def update(self,frame_time):
        if self.vector == (0,1):
            self.state = 0
        elif self.vector == (1,1):
            self.state = 1
        elif self.vector == (1,0):
            self.state = 2
        elif self.vector == (1,-1):
            self.state = 3
        elif self.vector == (0,-1):
            self.state = 4
        elif self.vector == (-1,-1):
            self.state = 5
        elif self.vector == (-1,0):
            self.state = 6
        elif self.vector == (-1,1):
            self.state = 7

        self.life_time += frame_time
        distance = Archer.RUN_SPEED_PPS * frame_time
        self.total_frames += Archer.FRAMES_PER_ACTION * Archer.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4 + self.motion
        if self.motion == 4:
            distance = 0
        else:
            self.x += self.vector[0] * distance
            self.y += self.vector[1] * distance


    def draw(self):
        self.image.clip_draw(self.state * 50, self.frame * 50, 50, 50,
                             self.x, self.y,self.size,self.size)
        for i in range(int(self.hp)):
            self.life_box.draw(self.x - 15 + i*2, self.y - 20,2,4)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    #사거리
    def get_rb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50


    def draw_rb(self):
        draw_rectangle(*self.get_rb())


class Knight:
    image = None
    life_box = None

    PIXEL_PER_METER = (10.0 / 0.5)                     # 10 pixel 50 cm
    RUN_SPEED_KMPH = 10.0                               # Km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.x, self.y = main_state.mx, main_state.my
        self.size = 60
        self.state = 2
        self.frame = 0
        self.motion = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.vector = (0, 1)

        self.hp = 20
        self.atk = 0.1

        if Knight.image == None:
            Knight.image = load_image('Images\\human_knight.png')
        if Knight.life_box == None:
            Knight.life_box = load_image('Images\\life.png')

    def update(self,frame_time):
        if self.vector == (0,1):
            self.state = 0
        elif self.vector == (1,1):
            self.state = 1
        elif self.vector == (1,0):
            self.state = 2
        elif self.vector == (1,-1):
            self.state = 3
        elif self.vector == (0,-1):
            self.state = 4
        elif self.vector == (-1,-1):
            self.state = 5
        elif self.vector == (-1,0):
            self.state = 6
        elif self.vector == (-1,1):
            self.state = 7

        self.life_time += frame_time
        distance = Knight.RUN_SPEED_PPS * frame_time
        self.total_frames += Knight.FRAMES_PER_ACTION * Knight.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4 + self.motion
        if self.motion == 4:
            distance = 0
        else:
            self.x += self.vector[0] * distance
            self.y += self.vector[1] * distance


    def draw(self):
        self.image.clip_draw(self.state * 50, self.frame * 50, 50, 50,
                             self.x, self.y,self.size,self.size)
        for i in range(int(self.hp)):
            self.life_box.draw(self.x - 15 + i*2, self.y - 20,2,4)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    #사거리
    def get_rb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


    def draw_rb(self):
        draw_rectangle(*self.get_rb())


class Mage:
    image = None
    life_box = None

    PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
    RUN_SPEED_KMPH = 4.0  # Km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.x, self.y = main_state.mx, main_state.my
        self.size = 50
        self.state = 2
        self.frame = 0
        self.motion = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.vector = (0, 1)

        self.hp = 10
        self.atk = 0.1

        if Mage.image == None:
            Mage.image = load_image('Images\\human_mage.png')
        if Mage.life_box == None:
            Mage.life_box = load_image('Images\\life.png')

    def update(self,frame_time):
        if self.vector == (0,1):
            self.state = 0
        elif self.vector == (1,1):
            self.state = 1
        elif self.vector == (1,0):
            self.state = 2
        elif self.vector == (1,-1):
            self.state = 3
        elif self.vector == (0,-1):
            self.state = 4
        elif self.vector == (-1,-1):
            self.state = 5
        elif self.vector == (-1,0):
            self.state = 6
        elif self.vector == (-1,1):
            self.state = 7

        self.life_time += frame_time
        distance = Mage.RUN_SPEED_PPS * frame_time
        self.total_frames += Mage.FRAMES_PER_ACTION * Mage.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4 + self.motion
        if self.motion == 4:
            distance = 0
        else:
           self.x += self.vector[0] * distance
           self.y += self.vector[1] * distance

    def draw(self):
        self.image.clip_draw(self.state * 50, self.frame * 50, 50, 50,
                             self.x, self.y,self.size,self.size)
        for i in range(int(self.hp)):
            self.life_box.draw(self.x - 15 + i * 2, self.y - 20, 2, 4)


    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    #사거리
    def get_rb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50


    def draw_rb(self):
        draw_rectangle(*self.get_rb())


class human_Tower:
    pass

class human_Castle:
    pass

#############  ORC  ###############

class Grunt:
    image = None
    life_box = None

    PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
    RUN_SPEED_KMPH = 4.0  # Km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.x, self.y = 350, 500
        self.size = 50
        self.state = 4
        self.frame = 0
        self.motion = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.vector = (0, -1)

        self.hp = 15
        self.atk = 0.5

        if Grunt.image == None:
            Grunt.image = load_image('Images\\orc_grunt.png')
        if Grunt.life_box == None:
            Grunt.life_box = load_image('Images\\life.png')

    def update(self, frame_time):
        if self.hp < 0 :
            main_state.enemyList.remove(self)

        if self.vector == (0, 1):
            self.state = 0
        elif self.vector == (1, 1):
            self.state = 1
        elif self.vector == (1, 0):
            self.state = 2
        elif self.vector == (1, -1):
            self.state = 3
        elif self.vector == (0, -1):
            self.state = 4
        elif self.vector == (-1, -1):
            self.state = 5
        elif self.vector == (-1, 0):
            self.state = 6
        elif self.vector == (-1, 1):
            self.state = 7

        for unit in main_state.unitList:
            if main_state.collide(unit, self):
                self.motion = 4
                if self.frame == 4:
                    unit.hp -= self.atk
            else:
                self.motion = 0

        self.life_time += frame_time
        distance = Grunt.RUN_SPEED_PPS * frame_time
        self.total_frames += Grunt.FRAMES_PER_ACTION * Grunt.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4 + self.motion
        if self.motion == 4:
            distance = 0
        else:
            self.x += self.vector[0] * distance
            self.y += self.vector[1] * distance

    def draw(self):
        self.image.clip_draw(self.state * 50, self.frame * 50, 50, 50,
                             self.x, self.y, self.size, self.size)
        for i in range(int(self.hp)):
            self.life_box.draw(self.x - 15 + i * 2, self.y + 20, 2, 4)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    # 사거리
    def get_rb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_rb(self):
        draw_rectangle(*self.get_rb())



class Troll:
    pass

class Ogre:
    pass

class Death_kinght:
    pass

class orc_Tower:
    image = None
    missile = None
    life = None

    def __init__(self):
        self.x, self.y = 230, 520
        self.size = 40

        self.hp = 100
        self.atk = 1

        if orc_Tower.image == None:
            orc_Tower.image =  load_image('Images\\orc_tower.png')


    def draw(self):
        self.image.draw(self.x,self.y)


    def get_bb(self):
        return self.x - 30, self.y - 40, self.x + 30, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    #사거리
    def get_rb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100


    def draw_rb(self):
        draw_rectangle(*self.get_rb())



class orc_Castle:
    pass
