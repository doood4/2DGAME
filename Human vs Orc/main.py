from pico2d import *


# Game object class here
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas(800 ,720)
running = True


# game main loop code
while running:
    handle_events()

    clear_canvas()

    update_canvas()

    delay(0.05)

# finalization code
close_canvas()