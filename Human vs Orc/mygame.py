from pico2d import *
import game_framework
import start_state
import main_state


open_canvas(580,680,sync=True)
hide_cursor()

game_framework.run(main_state)