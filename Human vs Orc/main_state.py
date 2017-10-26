from pico2d import *
from Unit_Class import *
import game_framework
import title_state
import pause_state

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q: pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w: pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e: pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r: pass


def update():
   global timer
   footman1.update()
   if(timer > 20):
       footman2.update()
   if(timer > 40):
       knight.update()
   delay(0.1)
   timer += 1

def draw_scene():
    back_frame.draw(360, 360)
    footman1.draw()
    if timer > 20:
        footman2.draw()
    if timer > 40:
        knight.draw()

def draw():
    clear_canvas()
    draw_scene()
    update_canvas()




