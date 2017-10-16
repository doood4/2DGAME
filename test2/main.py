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
open_canvas(720 ,720)
running = True
test2 = load_image('test2.png')


# game main loop code
while running:
    handle_events()

    clear_canvas()

    #게임틀
    test2.draw(360,360)
    #진영

    #다리


    #휴먼 본진

    #휴먼 타워1

    #휴먼 타워2


    #오크 본진

    #오크 타워1

    #오크 타워2


    update_canvas()

    delay(0.05)

# finalization code
close_canvas()