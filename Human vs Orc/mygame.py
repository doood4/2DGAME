from pico2d import *
import game_framework
import main_state
import result_state

open_canvas(580,680,sync=True)
hide_cursor()

game_framework.run(main_state)