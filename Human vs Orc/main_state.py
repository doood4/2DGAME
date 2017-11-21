from pico2d import *
import random
from Unit_Class import *
from Object_Class import *
import Ai
import game_framework
import title_state
import pause_state
import result_state

name = "MainState"

# 시간 상수
current_time = 0.0
TIME = 0
timer = 0

# 마우스 상수
mx = 0
my = 0
ms = 0
click = False
build = True

# 카드 설정 상수
card_type = 0
card_no = 0

# 게임 변수
Gold = 50000
Human_Score = 0
Orc_Score = 0
selection = -1

orc_t1 = 0
orc_t2 = 0

# 이미지
cursor = None
map = None
back_frame = None
commandbar = None
qwer = None
sqwer = None
numbers = None
unitselect = None

######### 리스트 #######
enemyList = []
peasantList= []
unitList = []
buildingList= []
cardList = []
numList = [1, 2, 3, 4, 5]
########################

def TIMER():
    global TIME
    TIME = int(get_time())

# 숫자그리는 함수(변수,좌표)
def draw_number(A,x,y):

    i = 10
    Num = []
    count =0
    font = load_image('Images\\numbers.png')
    if A == 0:
        font.clip_draw(0 * 20, 0, 20, 20, x, y)
    else:
        while A != 0:
            a = A % i
            Num.append(a)
            A = (A - a) // 10
            count += 1

        for n in range(count):
            font.clip_draw(Num[n] * 20, 0, 20, 20, x - 10 * n, y)

# 카드 그리기
def draw_cards():
    global cardList

    #current
    for i in range(4):
        cardList[i].image.clip_draw(cardList[i].type * 60, 0, 60,80,70,350 - cardList[i].no*100)

    #next
    cardList[4].image.clip_draw(cardList[4].type*60,0,60,80,70,440,40,60)


# 카드 초기 설정
def init_cards():
    global numList,cardList,card_type,card_no

    for i in range(5):
        if i == 3:
            card_type = 0
            card_no = i
            card = Card()
            cardList.append(card)
        else:
            x = random.randint(0, len(numList) - 1)
            card_type = numList[x]
            card_no = i
            card = Card()
            cardList.append(card)
            numList.remove(card_type)


# 카드 바꾸기
def change_card():
    global selection, cardList, numList, card_no, card_type, Gold

    numList.append(cardList[selection].type)
    Gold -= cardList[selection].cost
    cardList[selection].type = cardList[4].type
    cardList[selection].cost = cardList[4].cost
    del (cardList[4])
    x = random.randint(0, len(numList) - 1)
    card_type = numList[x]
    card_no = 4
    card = Card()
    cardList.append(card)
    numList.remove(card_type)

# 유닛 빌드여부
def unit_build():
    global mx, my, selection, cardList, unitselect, build, Gold

    if mx > 150 and mx < 530 and my < 300 and my > 120 and Gold >= cardList[selection].cost:
        build = True
    else:
        build = False

    if selection != -1 and mx > 130 :
        unitselect.clip_draw(100 * (cardList[selection].type - 1), 100 - 100*build, 100, 100, mx, my)

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def collide(a, b):
    # fill here
    left_a,bottom_a,right_a,top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return  False
    if right_a < left_b: return False
    if top_a < bottom_b: return  False
    if bottom_a > top_b: return  False

    return True

def range_collide(ra, b):
    left_a,bottom_a,right_a,top_a = ra.get_rb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return  False
    if right_a < left_b: return False
    if top_a < bottom_b: return  False
    if bottom_a > top_b: return  False

    return True

def agro_collide(ab,b):
    left_a, bottom_a, right_a, top_a = ab.get_ab()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def create_world():
    global peasantList, commandbar, qwer, sqwer, unitselect, back_frame, cursor, cardList, card_type, card_no, \
        enemyList, map

    # 시작 일꾼
    peasant = Peasant()
    peasantList.append(peasant)

    # 시작 건물 배치
    castle = orc_Castle()
    enemyList.append(castle)
    castle = human_Castle()
    unitList.append(castle)
    buildingList.append(castle)

    tower1 = orc_Tower1()
    tower2 = orc_Tower2()
    enemyList.append(tower1)
    enemyList.append(tower2)

    tower1 = human_Tower1()
    tower2 = human_Tower2()
    unitList.append(tower1)
    unitList.append(tower2)
    buildingList.append(tower1)
    buildingList.append(tower2)

    # 시작 카드 설정
    init_cards()

    map = load_image('1c.png')
    back_frame = load_image('Images\\back.png')
    commandbar = load_image('Images\\commandbar_frame.png')
    qwer = load_image('Images\\qwer.png')
    sqwer = load_image('Images\\sqwer.png')
    unitselect = load_image('Images\\unitselect.png')
    cursor = load_image('Images\\cursor.png')


def destroy_world():
    global cursor, back_frame

    del (back_frame)
    del (cursor)


def enter():
    create_world()


def exit():
    destroy_world()


def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global mx,my,click,unitselect,build,peasantList,Gold,selection,card_type,card_no

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mx = event.x
            my = 680 - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_p:
                game_framework.push_state(result_state)

            elif event.key == SDLK_q:
                if selection == 0:
                    selection = -1
                else:
                    selection= 0

            elif event.key == SDLK_w:
                if selection == 1:
                    selection = -1
                else:
                    selection = 1

            elif event.key == SDLK_e:
                if selection == 2:
                    selection = -1
                else:
                    selection = 2
            # 일꾼
            elif event.key == SDLK_r:
                if selection == 3:
                    selection = -1
                else:
                    selection = 3
                    if Gold >= 50:
                        Gold -= 50
                        peasant = Peasant()
                        peasantList.append(peasant)
                        selection = -1

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                click = True
                # q클릭
                if mx > 40 and mx < 100 and my > 310 and my < 390:
                    if selection == 0:
                        selection = -1
                    else:
                        selection = 0
                        if Gold >= cardList[selection].cost:
                            # 일꾼
                            if cardList[selection].type == 0:
                                peasant = Peasant()
                                peasantList.append(peasant)
                                change_card()
                                selection = -1
                # w클릭
                if mx > 40 and mx < 100 and my > 210 and my < 290:
                    if selection == 1:
                        selection = -1
                    else:
                        selection = 1
                        if Gold >= cardList[selection].cost:
                            # 일꾼
                            if cardList[selection].type == 0:
                                peasant = Peasant()
                                peasantList.append(peasant)
                                change_card()
                                selection = -1
                # e클릭
                if mx > 40 and mx < 100 and my > 110 and my < 190:
                    if selection == 2:
                        selection = -1
                    else:
                        selection = 2
                        if Gold >= cardList[selection].cost:
                            # 일꾼
                            if cardList[selection].type == 0:
                                peasant = Peasant()
                                peasantList.append(peasant)
                                change_card()
                                selection = -1
                # r클릭
                if mx > 40 and mx < 100 and my > 10 and my <90:
                    if selection == 3:
                        selection = -1
                    else:
                        selection = 3
                        if Gold >= cardList[selection].cost:
                            # 일꾼
                            if cardList[selection].type == 0:
                                peasant = Peasant()
                                peasantList.append(peasant)
                                change_card()
                                selection = -1
                # 유닛 소환
                if selection != -1 and build is True:
                    if cardList[selection].type == 1:
                        unit = Footman()
                        unitList.insert(0,unit)
                        change_card()
                        selection = -1
                    elif cardList[selection].type == 2:
                        unit = Archer()
                        unitList.insert(0,unit)
                        change_card()
                        selection = -1
                    elif cardList[selection].type == 3:
                        unit = Knight()
                        unitList.insert(0,unit)
                        change_card()
                        selection = -1
                    elif cardList[selection].type == 4:
                        unit = Mage()
                        unitList.insert(0,unit)
                        change_card()
                        selection = -1
                    elif cardList[selection].type == 5:
                        unit = Gryphon()
                        unitList.insert(0,unit)
                        change_card()
                        selection = -1

        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                click = False


def update(frame_time):
    # 게임 종료 조건
    if Human_Score == 3 or Orc_Score == 3:
        game_framework.push_state(pause_state)
    if TIME == 300:
        game_framework.push_state(pause_state)

    # 시간 체크
    TIMER()

    # 컴퓨터 Ai
    Ai.ai()

    # 적
    for enemy in enemyList:
        enemy.update(frame_time)

    # 아군
    for unit in unitList:
       unit.update(frame_time)

    # 일꾼
    for peasant in peasantList:
       peasant.update(frame_time)


def draw_scene():

    back_frame.draw(290, 340, 580, 680)
    #map.draw(120+230,340,460,680)

    commandbar.draw(60, 340, 120, 680)
    qwer.draw(60,250)
    # 타이머
    draw_number(int((180 - TIME) / 60), 50, 630)
    draw_number(int(180 - TIME) % 60, 80, 630)
    #draw_number(TIME, 80, 630)

    # 휴먼 점수
    draw_number(Human_Score, 100, 580)
    # 오크 점수
    draw_number(Orc_Score, 100, 550)
    # 글로벌 골드
    draw_number(Gold, 100, 520)

    # 카드 그리기
    draw_cards()

    if selection > -1:
        sqwer.clip_draw(0, 300 - 100*selection, 120, 100, 60, 350 - 100*selection)

    #for enemy in enemyList:
    #    enemy.draw()
    #    enemy.draw_bb()
    #    enemy.draw_rb()

    # 적 그리기
    for enemy in enemyList:
        enemy.draw()
        #enemy.draw_bb()
        #enemy.draw_rb()
        #enemy.draw_ab()

    # 아군 그리기
    for unit in unitList:
        unit.draw()
        #unit.draw_bb()
        #unit.draw_rb()
        #unit.draw_ab()

    # 아군 건물 그리기
    for building in buildingList:
        building.draw()

    # 일꾼 그리기
    for peasant in peasantList:
        peasant.draw()

    # 빌드여부 그리기기
    unit_build()




def draw(frame_time):
    clear_canvas()

    draw_scene()

    # 커서는 최후방
    cursor.clip_draw(click * 50, 0, 50, 50, mx, my, 40, 40)

    update_canvas()




