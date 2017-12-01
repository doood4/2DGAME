from pico2d import *
import Unit_Class
import main_state

summon_x = 0
summon_y = 0

def ai():
    global summon_x, summon_y

    # 지속적으로 그런트 소환
    if main_state.TIME % 15 == 0 and get_time() - main_state.current_time - main_state.TIME > 0.01 \
            and get_time() - main_state.current_time - main_state.TIME < 0.03:
        for i in range(4):
            summon_x = i * 100 + 200
            summon_y = 450
            if i == 0:
                enemy = Unit_Class.Grunt()
                main_state.enemyList.append(enemy)
            elif i == 1:
                enemy = Unit_Class.Troll()
                main_state.enemyList.append(enemy)
            elif i == 2:
                enemy = Unit_Class.Death_kinght()
                main_state.enemyList.append(enemy)
            elif i == 3:
                enemy = Unit_Class.Ogre()
                main_state.enemyList.append(enemy)


    ## 지속적으로 트롤 소환
    #if main_state.TIME % 10 == 0 and get_time() - main_state.current_time - main_state.TIME > 0.01 \
    #        and get_time() - main_state.current_time - main_state.TIME < 0.03:
    #    for i in range(2):
    #        summon_x = i*300 + 200
    #        summon_y = 600
    #        enemy = Unit_Class.Troll()
    #        main_state.enemyList.append(enemy)
#
    ## 지속적으로 오우거 , 데스나이트 소환
    #if main_state.TIME % 15 == 0 and get_time() - main_state.current_time - main_state.TIME > 0.01 \
    #        and get_time() - main_state.current_time - main_state.TIME < 0.03:
    #    summon_x = 230
    #    summon_y = 480
    #    enemy = Unit_Class.Ogre()
    #    main_state.enemyList.append(enemy)
#
    #    summon_x = 450
    #    summon_y = 480
    #    enemy = Unit_Class.Ogre()
    #    main_state.enemyList.append(enemy)
#
    #    summon_x = 340
    #    summon_y = 480
    #    enemy = Unit_Class.Death_kinght()
    #    main_state.enemyList.append(enemy)


    # 타워 깨지면 데빌 소한
    #if main_state.orc_t1 == 1:
    #    main_state.orc_t1 = 0
    #    summon_x = 230
    #    summon_y = 520
    #    enemy = Unit_Class.Devil()
    #    main_state.enemyList.append(enemy)
#
    #if main_state.orc_t2 == 1:
    #    main_state.orc_t2 = 0
    #    summon_x = 450
    #    summon_y = 520
    #    enemy = Unit_Class.Devil()
    #    main_state.enemyList.append(enemy)



