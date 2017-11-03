from pico2d import *
import random
from Unit_Class import *
from Object_Class import *
import game_framework
import title_state
import pause_state


name = "MainState"

mx = 0
my = 0

gold = 50

cursor = None
click = False

back_frame = None
commandbar = None

peasantList= []

map = None
card = None
cardList = []

timer = 0

def enter():
    global peasantList,commandbar,back_frame,cursor,card,cardList

    peasant = Peasant()
    peasantList.append(peasant)

    back_frame = load_image('back_frame.png')
    commandbar = load_image('Images\\commandbar.png')
    cursor = load_image('Images\\cursor.png')

def exit():
    global peasant,footman1,footman2,knight,cursor

    del(peasant)
    del(back_frame)
    del(cursor)

def pause():
    pass

def resume():
    pass


def handle_events():
    global mx,my,click,peasantList

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION :
            mx = event.x
            my = 720 - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                pass
            elif event.key == SDLK_p:
                game_framework.push_state(pause_state)
            elif event.key == SDLK_q:
                peasant = Peasant()
                peasantList.append(peasant)

                pass
            elif event.key == SDLK_w:
                pass
            elif event.key == SDLK_e:
                pass
            elif event.key == SDLK_r:
                pass
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                click = True

        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                click = False



def update():
   global timer
   for peasant in peasantList:
       peasant.update()

   delay(0.1)
   timer += 1

def draw_scene():
    back_frame.draw(360, 360, 720, 720)
    commandbar.draw(600,60 , 400, 120)

    for peasant in peasantList:
        peasant.draw()

    # 커서는 최후방
    cursor.clip_draw(click * 50, 0, 50, 50, mx, my, 40, 40)


def draw():
    clear_canvas()
    draw_scene()
    update_canvas()




