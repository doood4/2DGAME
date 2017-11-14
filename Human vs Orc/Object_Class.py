from pico2d import *
import main_state

class Card:
    image = None

    def __init__(self):
        self.type = main_state.card_type
        self.no = main_state.card_no
        if self.type == 0: # 일꾼
            self.cost = 50
        elif self.type == 1: # 풋맨
            self.cost = 50
        elif self.type == 2: # 아처
            self.cost = 50
        elif self.type == 3: # 나이트
            self.cost = 50
        elif self.type == 4: # 메이지
            self.cost = 50
        elif self.type == 5: # 그리폰
            self.cost = 50

        self.xsize = 60
        self.ysize = 80

        if Card.image == None:
            Card.image = load_image('Images\\human_cards.png')

    def update(self):
        pass

    def draw(self):
        pass


