from pico2d import *
import random
import main_state



#############  HUMAN  ###############

class Peasant:

    image = None
    plus10 = None

    PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
    RUN_SPEED_KMPH = 20.0  # Km/h
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

        if self.x > 510 and self.y == 15:
            self.vector = (-1,0)
            self.y += 30
        elif self.x < 350 and self.y == 45:
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
        self.x_vector = 0
        self.y_vector = 1

        self.hp = 15
        self.atk = 0.1

        if Footman.image == None:
            Footman.image = load_image('Images\\human_footman.png')
        if Footman.life_box == None:
            Footman.life_box = load_image('Images\\life.png')


    def update(self,frame_time):
        # 자동 이동 목표
        for enemy in main_state.enemyList:
            if not main_state.range_collide(self,enemy):
                if self.x < 350:
                    if self.x > 240:
                        self.x_vector = -1
                        self.y_vector = 1

                    elif self.x < 220:
                        self.x_vector = 1
                        self.y_vector = 1

                    else:
                        self.x_vector = 0
                        self.y_vector = 1

                else:
                    if self.x > 460:
                        self.x_vector = -1
                        self.y_vector = 1

                    elif self.x < 440:
                        self.x_vector = 1
                        self.y_vector = 1

                    else:
                        self.x_vector = 0
                        self.y_vector = 1

        # 공격하러 이동
        for enemy in main_state.enemyList:
            if main_state.range_collide(self,enemy):
                if self.x > enemy.x + 10:
                    self.x_vector = -1
                    if self.y > enemy.y + 10:
                        self.y_vector = -1
                        break
                    elif self.y < enemy.y - 10:
                        self.y_vector = 1
                        break
                    else:
                        self.y_vector = 0
                        break
                elif self.x < enemy.x - 10:
                    self.x_vector = 1
                    if self.y > enemy.y + 10:
                        self.y_vector = -1
                        break
                    elif self.y < enemy.y - 10:
                        self.y_vector = 1
                        break
                    else:
                        self.y_vector = 0
                        break
                else:
                    self.x_vector = 0
                    if self.y > enemy.y + 10:
                        self.y_vector = -1
                        break
                    elif self.y < enemy.y - 10:
                        self.y_vector = 1
                        break
                    else:
                        self.y_vector = 0
                        break


        if self.x_vector == 0 and self.y_vector == 1:
            self.state = 0
        elif self.x_vector == 1 and self.y_vector == 1:
            self.state = 1
        elif self.x_vector == 1 and self.y_vector == 0:
            self.state = 2
        elif self.x_vector == 1 and self.y_vector == -1:
            self.state = 3
        elif self.x_vector == 0 and self.y_vector == -1:
            self.state = 4
        elif self.x_vector == -1 and self.y_vector == -1:
            self.state = 5
        elif self.x_vector == -1 and self.y_vector == 0:
            self.state = 6
        elif self.x_vector == -1 and self.y_vector == 1:
            self.state = 7

        # 공격대상 없다
        for enemy in main_state.enemyList:
            if not main_state.collide(enemy,self):
                self.motion = 0
        # 공격대상 있다
        for enemy in main_state.enemyList:
            if main_state.collide(enemy, self):
                self.motion = 4
                if self.frame == 4:
                    enemy.hp -= self.atk
                    break

         # 죽음
        if self.hp <= 0:
            self.motion = 8

        self.life_time += frame_time
        distance = Footman.RUN_SPEED_PPS * frame_time
        self.total_frames += Footman.FRAMES_PER_ACTION * Footman.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4 + self.motion
        if self.frame == 10:
            main_state.unitList.remove(self)

        if self.motion == 4:
            distance = 0
        elif self.motion == 8:
            distance = 0
        else:
            self.x += self.x_vector * distance
            self.y += self.y_vector * distance

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

class Bomb:
    PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
    RUN_SPEED_KMPH = 80  # Km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0
        self.x_vector = 0
        self.y_vector = 1

        if Bomb.image == None:
            Bomb.image = load_image('Images\\bomb.png')

    def init(self,tower,enemy):
        self.x = tower.x
        self.y = tower.y
        self.target_x = enemy.x
        self.target_y = enemy.y

    def update(self, frame_time):
        if self.x > self.target_x - 10 and self.x < self.target_x + 10 and self.y > self.target_y - 10 and self.y < self.target_y + 10:
            main_state.arrowList.remove(self)

        if self.x < self.target_x:
            self.x_vector = 1
        elif self.x > self.target_x:
            self.x_vector = -1

        distance = Bomb.RUN_SPEED_PPS * frame_time
        self.x += self.x_vector * distance
        self.y += self.y_vector * distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    # 사거리
    def get_rb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100

    def draw_rb(self):
        draw_rectangle(*self.get_rb())
    pass

class human_Tower1:
    image = None
    life = None

    def __init__(self):
        self.x = 230
        self.y = 160

        self.hp = 100
        self.atk = 1

        if human_Tower1.image == None:
            human_Tower1.image = load_image('Images\\human_tower.png')

    def update(self, frame_time):
        for enemy in main_state.enemyList:
            if main_state.range_collide(self,enemy):
                bomb = Bomb()
                bomb.init(self.x,self.y,enemy)
                main_state.arrowList.append(bomb)
                break


    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 40, self.x + 30, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    # 사거리
    def get_rb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100

    def draw_rb(self):
        draw_rectangle(*self.get_rb())


class human_Tower2:
    image = None
    life = None

    def __init__(self):
        self.x = 450
        self.y = 160

        self.hp = 100
        self.atk = 10

        if human_Tower2.image == None:
            human_Tower2.image = load_image('Images\\human_tower.png')

    def update(self, frame_time):
        if main_state.TIME % 2 == 0 and get_time() - main_state.TIME > 0.01 and get_time() - main_state.TIME < 0.03:
            for enemy in main_state.enemyList:
                 if main_state.range_collide(self,enemy):
                      bomb = Bomb()
                      bomb.init(self,enemy)
                      main_state.arrowList.append(bomb)
                      enemy.hp -= self.atk
                      break

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 40, self.x + 30, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    # 사거리
    def get_rb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100

    def draw_rb(self):
        draw_rectangle(*self.get_rb())


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
        self.x, self.y = random.randint(400, 500), random.randint(400, 500)
        self.size = 50
        self.state = 4
        self.frame = 0
        self.motion = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.x_vector = 0
        self.y_vector = -1

        self.hp = 15
        self.atk = 0.1

        if Grunt.image == None:
            Grunt.image = load_image('Images\\orc_grunt.png')
        if Grunt.life_box == None:
            Grunt.life_box = load_image('Images\\life.png')

    def update(self, frame_time):
        # 자동 이동 목표
        for unit in main_state.unitList:
            if not main_state.range_collide(self, unit):
                if self.x < 350:
                    if self.x > 240:
                        self.x_vector = -1
                        self.y_vector = -1

                    elif self.x < 220:
                        self.x_vector = 1
                        self.y_vector = -1

                    else:
                        self.x_vector = 0
                        self.y_vector = -1

                else:
                    if self.x > 460:
                        self.x_vector = -1
                        self.y_vector = -1

                    elif self.x < 440:
                        self.x_vector = 1
                        self.y_vector = -1

                    else:
                        self.x_vector = 0
                        self.y_vector = -1

        # 공격하러 이동
        for unit in main_state.unitList:
            if main_state.range_collide(self, unit):
                if self.x > unit.x + 10:
                    self.x_vector = -1
                    if self.y > unit.y + 10:
                        self.y_vector = -1
                        break
                    elif self.y < unit.y - 10:
                        self.y_vector = 1
                        break
                    else:
                        self.y_vector = 0
                        break
                elif self.x < unit.x - 10:
                    self.x_vector = 1
                    if self.y > unit.y + 10:
                        self.y_vector = -1
                        break
                    elif self.y < unit.y - 10:
                        self.y_vector = 1
                        break
                    else:
                        self.y_vector = 0
                        break
                else:
                    self.x_vector = 0
                    if self.y > unit.y + 10:
                        self.y_vector = -1
                        break
                    elif self.y < unit.y - 10:
                        self.y_vector = 1
                        break
                    else:
                        self.y_vector = 0
                        break

        if self.x_vector == 0 and self.y_vector == 1:
            self.state = 0
        elif self.x_vector == 1 and self.y_vector == 1:
            self.state = 1
        elif self.x_vector == 1 and self.y_vector == 0:
            self.state = 2
        elif self.x_vector == 1 and self.y_vector == -1:
            self.state = 3
        elif self.x_vector == 0 and self.y_vector == -1:
            self.state = 4
        elif self.x_vector == -1 and self.y_vector == -1:
            self.state = 5
        elif self.x_vector == -1 and self.y_vector == 0:
            self.state = 6
        elif self.x_vector == -1 and self.y_vector == 1:
            self.state = 7


        # 공격대상 없다
        for unit in main_state.unitList:
            if not main_state.collide(unit,self):
                self.motion = 0
        # 공격대상 있다
        for unit in main_state.unitList:
            if main_state.collide(unit, self):
                self.motion = 4
                if self.frame == 4:
                    unit.hp -= self.atk
                    break

        # 죽음
        if self.hp <= 0:
            self.motion = 8

        self.life_time += frame_time
        distance = Grunt.RUN_SPEED_PPS * frame_time
        self.total_frames += Grunt.FRAMES_PER_ACTION * Grunt.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4 + self.motion
        if self.frame == 10:
            main_state.enemyList.remove(self)

        if self.motion == 4:
            distance = 0
        elif self.motion == 8:
            distance = 0
        else:
            self.x += self.x_vector * distance
            self.y += self.y_vector * distance

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
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw_rb(self):
        draw_rectangle(*self.get_rb())


class Troll:
    pass

class Ogre:
    pass

class Death_kinght:
    pass

class orc_Tower1:
    image = None
    life = None

    def __init__(self):
        self.x = 230
        self.y = 520

        self.hp = 100
        self.atk = 1

        if orc_Tower1.image == None:
            orc_Tower1.image = load_image('Images\\orc_tower.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 40, self.x + 30, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    #사거리
    def get_rb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100


    def draw_rb(self):
        draw_rectangle(*self.get_rb())

class orc_Tower2:
    image = None
    life = None

    def __init__(self):
        self.x = 450
        self.y = 520

        self.hp = 100
        self.atk = 1

        if orc_Tower2.image == None:
            orc_Tower2.image = load_image('Images\\orc_tower.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

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
