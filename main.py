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

deck_srf = pg.Surface((120*scale, 36*scale))
deck_rect = deck_srf.get_rect()
deck_srf.fill(pink)

scale = 4
card_sheet = pg.image.load('card-sheet.png')
cards = []
for y in range(6):
    for x in range(6):
        init_card = pg.Surface((14, 19))
        init_card.blit(card_sheet, (0,0), (x*14, y*19, 14, 19))
        card = pg.transform.scale(init_card, (14*scale, 19*scale))
        cards.append(card)

card_group = pg.sprite.Sprite.group()
for x in range(4):
    card_rect = pg.Rect(0, 0, 14, 19)
    card = card_obj(card_rect, cards[x], deck_srf)
    card_group.add(card)

def main():
    loop = True
    while loop:
        scr.fill(bg_color)
        scr.blit(deck_srf, dead_cntr(deck_srf, dimen))
        card_group.update()
        #scr.blit(cards[6*1], dead_cntr(cards[0], dimen))
        pg.display.update()

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                loop = False
                break 
            elif ev.type == pg.KEYDOWN:
                pass
        clock.tick(fps)

main()