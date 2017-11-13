from pico2d import *
import main_state

class Card:
    image = None
    def __init__(self):
        self.type = main_state.card_type
        self.no = main_state.card_no
        self.cost = 20
        self.xsize = 60
        self.ysize = 80

        if Card.image == None:
            Card.image = load_image('Images\\human_cards.png')

    def update(self):
        pass

    def draw(self):
        pass


