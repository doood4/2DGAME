import main_state
import game_framework
from pico2d import *

name = "ResultState"

###########
mLight_x = 290
mLight_y = 0

mLight = None
victory = None



def enter():
    global mLight, victory
    victory = load_image('Images\\victory.png')
    mLight = load_image('Images\\button_light.png')


def exit():
    pass

def handle_events(frame_time):
    global mLight_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()
        elif event.type == SDL_MOUSEMOTION:
            main_state.mx = event.x
            main_state.my = 680 - event.y
            if main_state.mx > 190 and main_state.mx < 390:
                if main_state.my > 40 and main_state.my < 90:
                    mLight_y = 65
                elif main_state.my > 110 and main_state.my < 160:
                    mLight_y = 135
                elif main_state.my > 180 and main_state.my < 230:
                    mLight_y = 205
                else:
                    mLight_y = 0
            else:
                mLight_y = 0
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                main_state.click = True
                if main_state.mx > 190 and main_state.mx < 390:
                    if main_state.my > 40 and main_state.my < 90: #exit
                        game_framework.quit()
                    elif main_state.my > 110 and main_state.my < 160: #title
                        mLight_y = 135
                    elif main_state.my > 180 and main_state.my < 230: #re
                        game_framework.change_state(main_state)

        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                main_state.click = False

def draw(frame_time):
    clear_canvas()

    main_state.draw_scene()
    victory.draw(290,340)
    if mLight_y != 0:
        mLight.draw(mLight_x,mLight_y)

    main_state.cursor.clip_draw(main_state.click * 50, 0, 50, 50, main_state.mx, main_state.my, 40, 40)

    update_canvas()

def update(frame_time):
    pass

def pause():
    pass

def resume():
    pass
