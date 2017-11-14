from pico2d import *
from Unit_Class import *
import main_state


def Ai():

    if main_state.TIME % 10 == 0 and get_time() - main_state.TIME > 0.01 and get_time() - main_state.TIME < 0.02:
        grunt = Grunt()
        main_state.enemyList.append(grunt)
        troll = Troll()
        main_state.enemyList.append(troll)

    if main_state.TIME % 27 == 0 and get_time() - main_state.TIME > 0.01 and get_time() - main_state.TIME < 0.02:
        ogre = Ogre()
        main_state.enemyList.append(ogre)
        death = Death_kinght()
        main_state.enemyList.append(death)
