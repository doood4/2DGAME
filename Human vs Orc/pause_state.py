import main_state
import game_framework
from pico2d import *

name = "PauseState"

pauseimage = None

def enter():
    pass

def exit():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()

def draw(frame_time):
    clear_canvas()
    main_state.draw_scene()
    update_canvas()

def update(frame_time):
    pass

def pause():
    pass

def resume():
    pass
