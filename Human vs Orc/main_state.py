from pico2d import *
from Unit_Class import *
import game_framework
import title_state


name = "MainState"

footman1 = None
footman2 = None
knight = None
timer = 0

def enter():
    global footman1,footman2,knight
    footman1 = Footman()
    footman2 = Footman()
    knight = Knight()

def exit():
    global footman1,footman2,knight
    del(footman1)
    del(footman2)
    del(knight)

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
    footman1.draw()
    if timer > 20:
        footman2.draw()
    if timer > 40:
        knight.draw()
    update_canvas()







