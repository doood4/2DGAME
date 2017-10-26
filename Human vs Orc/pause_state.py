import main_state
import game_framework
from pico2d import *


name = "PauseState"

pauseimage = None

def enter():
    global pauseimage

    pauseimage = load_image('pause.png')

def exit(): pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()

def draw():
    clear_canvas()
    main_state.draw_scene()
    pauseimage.draw(400,360)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
