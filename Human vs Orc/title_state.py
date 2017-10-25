import game_framework
from pico2d import *
import main_state


name = "TitleState"

def enter(): pass

def exit(): pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def draw(): pass

def update():
    pass

def pause():
    pass

def resume():
    pass






