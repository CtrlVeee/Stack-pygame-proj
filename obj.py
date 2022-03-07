#place all funcs and obj definition here
import pygame as pg
dimen = (720, 576)
scale = 4
scr = pg.display.set_mode(dimen)
card_sheet = pg.image.load('card-sheet.png')
cards = []
for y in range(6):
    for x in range(6):
        init_card = pg.Surface((14, 19))
        init_card.blit(card_sheet, (0,0), (x*14, y*19, 14, 19))

        card = pg.transform.scale(init_card, (14*scale, 19*scale))
        cards.append(card)
#print(cards)

flipped_card = pg.image.load('flipped-card.png').convert_alpha()
flipped_card = pg.transform.scale(flipped_card, (14*scale, 17*scale))

def dead_cntr (scr, dim):
    x = abs(int((scr.get_width() - dim[0])/2))
    y = abs(int((scr.get_height() - dim[1])/2))
    return (x, y)

class card_obj:
    def __init__(self, placement, type):
        self.rect = placement
        self.type = type #what color and symbol
        self.hint_active = False
        self.face = 'face-down' #sets if flipped or not
        # the card objs will be updated through a sprite group

loop = True
while loop:
    scr.fill((23, 17, 26))

    scr.blit(cards[6*5], dead_cntr(cards[0], dimen))
    pg.display.update()
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            loop= False
            break