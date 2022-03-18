from tkinter import Button
import pygame as pg
from objects import *

#next task is enter button mecha

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

card_in_hover = 17
card_in_use = False
slot_data = [-1, -1, -1, -1]

def check_full(data):
    try:
        a = data.index(-1)
        return False
    except:
        return True

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

#make the card imgs
card_sheet = pg.image.load('card-sheet.png').convert_alpha()
cards = []

for pos in prior:
    init_card = pg.Surface((14, 19)).convert_alpha()
    init_card.blit(card_sheet, (0,0), (pos[0]*14, pos[1]*19, 14, 19))
    card = pg.transform.scale(init_card, (14*scale, 19*scale))
    cards.append(card)

#mouse mecha
def hover_func(rect, index):
    mos_pos = pg.mouse.get_pos()
    dx = mos_pos[0] - int(rect.width)/2
    dy = mos_pos[1] - int(rect.height)/2

    pressed = pg.mouse.get_pressed()[0]
    global card_in_hover
    global card_in_use

    if rect.collidepoint(mos_pos) and pressed:
        if not card_in_use:
            card_in_hover = index
        card_in_use = True
    if pressed:
        try:
            scr.blit(cards[card_in_hover], (dx, dy))
        except: 
            card_in_use = False
    if not pressed:
        card_in_hover = 17
        card_in_use = False

# make the card objects
#card_group = pg.sprite.Group() #--test so that i can access the items as a list
card_group = []
for x in range(8):
    card_rect = pg.Rect(x*15*scale, 0*scale, 14*scale, 17*scale)
    card = card_obj(card_rect, cards[x], x, deck_pos, scr)
    #card_group.add(card)
    card_group.append(card)

for y in range(8):
    card_rect = pg.Rect(y*15*scale, 18*scale, 14*scale, 17*scale)
    card = card_obj(card_rect, cards[y+8], y+8, deck_pos, scr)
    #card_group.add(card)
    card_group.append(card)

def update_deck(data):
    global card_group
    for val in data:
        if val == -1:
            card_group[val].in_use = False
        elif val != -1:
            card_group[val].in_use = True


#make the table obj
table_x = int((scr_w - 94*scale)/2) 
table_y = int((scr_h - 37*scale)/2) - 80
Table = table_obj((table_x, table_y))

#make buttons here
enter_sheet = pg.image.load("enter-button.png").convert_alpha()
enter_pos = dead_cntr(enter_sheet, dimen)
enter_pos[0] -= 5*scale
enter_pos[1] -= 4*scale
Enter_button = button(enter_pos, enter_sheet)

def main():
    global slot_data
    global card_group
    loop = True
    while loop:
        #print(slot_data)
        scr.fill(bg_color)
        slot_data = Table.blit(scr, card_in_hover, card_in_use)

        if slot_data != [-1, -1, -1, -1]:
            Table.active_state = True
        else:
            Table.active_state = False
        if check_full(slot_data):
            Enter_button.update(scr)

        scr.blit(deck_srf, deck_pos)
        deck_srf.fill(bg_color)
        for card in card_group:
            for val in slot_data:
                if card.marker == val:
                    card.in_use = True
                    break
                else:
                    card.in_use = False
                    continue
            if card_in_use:
                card.hover = False
            card.update(card_in_use)
            if not card.in_use:
                hover_func(card.apparent_rect, card.marker)
        
        pg.display.update()

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                loop = False
                break 
            elif ev.type == pg.KEYDOWN:
                pass
        clock.tick(fps)

main()