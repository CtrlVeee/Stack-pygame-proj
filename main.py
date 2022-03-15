import pygame as pg
from objects import *

pg.init()
#convert all sprites to 4x size
scr_w = 720
scr_h = 576
dimen = (scr_w, scr_h)
scr = pg.display.set_mode((scr_w, scr_h))

scale = 4
fps = 30
clock = pg.time.Clock()
bg_color = pg.Color(23, 17, 26)
pink = pg.Color(255, 128, 170)

#surface for the deck selection
deck_srf = pg.Surface((119*scale, 36*scale)).convert_alpha()
deck_rect = deck_srf.get_rect()
deck_pos = dead_cntr(deck_srf, dimen)
deck_pos[1] = scr_h - (56*scale)

prior = [
    [0,0], [3, 0], [4, 0], [1,0],
    [0,1], [3, 1], [4, 1], [1,1],
    [0,5], [3, 5], [4, 5], [1,5],
    [0,2], [3, 2], [4, 2], [1,2]
]

scale = 4
card_sheet = pg.image.load('card-sheet.png').convert_alpha()
cards = []

for pos in prior:
    init_card = pg.Surface((14, 19)).convert_alpha()
    init_card.blit(card_sheet, (0,0), (pos[0]*14, pos[1]*19, 14, 19))
    card = pg.transform.scale(init_card, (14*scale, 19*scale))
    cards.append(card)

# make the card selection
card_group = pg.sprite.Group()
for x in range(8):
    card_rect = pg.Rect(x*15*scale, 0*scale, 14*scale, 17*scale)
    card = card_obj(card_rect, cards[x], deck_srf, deck_pos, scr)
    card_group.add(card)

for y in range(8):
    card_rect = pg.Rect(y*15*scale, 18*scale, 14*scale, 17*scale)
    card = card_obj(card_rect, cards[y+8], deck_srf, deck_pos, scr)
    card_group.add(card)

#make the table obj
table_x = int((scr_w - 94*scale)/2) 
table_y = int((scr_h - 37*scale)/2) - 80
Table = table_obj((table_x, table_y))

def main():
    loop = True
    while loop:
        scr.fill(bg_color)
        scr.blit(deck_srf, deck_pos)
        deck_srf.fill(bg_color)
        card_group.update()
        #scr.blit(cards[6*1], dead_cntr(cards[0], dimen))
        Table.blit(scr)
        pg.display.update()

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                loop = False
                break 
            elif ev.type == pg.KEYDOWN:
                pass
        clock.tick(fps)

main()