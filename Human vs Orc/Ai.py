from pico2d import *
from Unit_Class import *
import main_state


def Ai():

    if main_state.TIME % 5 == 0 and get_time() - main_state.TIME > 0.01 and get_time() - main_state.TIME < 0.02:
        enemy = Grunt()
        main_state.enemyList.append(enemy)
        enemy = Grunt()
        main_state.enemyList.append(enemy)
        enemy = Troll()
        main_state.enemyList.append(enemy)
        enemy = Ogre()
        main_state.enemyList.append(enemy)



        #troll = Troll()
        #main_state.enemyList.append(troll)

        #troll = Troll()
        #main_state.enemyList.append(troll)
        #devil = Devil()
        #main_state.enemyList.append(devil)


    if main_state.TIME % 10 == 0 and get_time() - main_state.TIME > 0.01 and get_time() - main_state.TIME < 0.02:
        enemy = Death_kinght()
        main_state.enemyList.append(enemy)
        enemy = Devil()
        main_state.enemyList.append(enemy)







