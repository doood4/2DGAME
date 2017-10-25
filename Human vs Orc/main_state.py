from pico2d import *
from Unit_Class import *
import game_framework
import title_state

name = "MainState"

back_frame = None
footman1 = None
footman2 = None
knight = None
timer = 0

def enter():
    global footman1,footman2,knight,back_frame
    footman1 = Footman()
    footman2 = Footman()
    knight = Knight()
    back_frame = load_image('back_frame.png')

def exit():
    global footman1,footman2,knight
    del(footman1)
    del(footman2)
    del(knight)
    del(back_frame)

def pause():
    pass

def resume():
    pass


def handle_events():
    events =get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


def update():
   global timer
   footman1.update()
   if(timer > 20):
       footman2.update()
   if(timer > 40):
       knight.update()
   delay(0.1)
   timer += 1

def draw():
    clear_canvas()
    back_frame.draw(400, 360)
    footman1.draw()
    if timer > 20:
        footman2.draw()
    if timer > 40:
        knight.draw()
    update_canvas()







