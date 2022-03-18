#use for 
#fix deck card mechanism---done
#change card sheet from 36 cards to 16---done
# new task: if card is in use, blit empty card instead (deck)
# if all data in data list is not -1, blit the algo button

#from math import fabs
import pygame as pg

scale = 4

def dead_cntr (scr, dim):
    x = abs(int((scr.get_width() - dim[0])/2))
    y = abs(int((scr.get_height() - dim[1])/2))
    return [x, y]


class card_obj(pg.sprite.Sprite):
    def __init__(self, rect_data, kindOf, int_val, deckPos, screen):
        pg.sprite.Sprite.__init__(self)
        self.rect = rect_data 
        self.img = kindOf #what color and symbol

        flipped_img = pg.image.load("flipped-card.png").convert_alpha()
        self.flipped_img = pg.transform.scale(flipped_img, (14*scale, 17*scale))

        empty_img = pg.image.load("empty-card.png").convert_alpha()
        self.empty_img = pg.transform.scale(empty_img, (14*scale, 17*scale))

        self.blit_img = self.flipped_img
        self.blit_srf = screen
        self.screen = screen

        self.marker = int_val
        self.hint_active = False
        self.hover = False #tracks if mouse hovers over card
        self.in_use = False #sets if the deck shows an empty-card or a flipped one
        self.grab = False

        self.deckPos = deckPos

        new_x = self.rect.x + self.deckPos[0]
        new_y = self.rect.y + self.deckPos[1]
        self.apparent_rect = pg.Rect(new_x, new_y, self.rect.w, self.rect.h)
        hover_y = self.apparent_rect.y - 6*scale
        self.hover_rect = pg.Rect(self.apparent_rect.x, hover_y, self.rect.w, self.rect.h)

        # the card objs will be updated through a sprite group
    def mouse_track(self, in_use):
        mos_pos = pg.mouse.get_pos()

        if self.apparent_rect.collidepoint(mos_pos) and not in_use:
            self.hover = True
        else:
            self.hover = False
    
    def update(self, in_use):
        if self.in_use:
            self.blit_img = self.empty_img
        elif not self.in_use:
            self.blit_img = self.flipped_img
            self.mouse_track(in_use)
        self.blit_srf.blit(self.blit_img, self.apparent_rect)
        if self.hover:            
            self.blit_srf.blit(self.img, self.hover_rect)

class table_obj:
    def __init__(self, pos):
        #init all img
        self.img = pg.image.load("slot-table.png").convert_alpha()
        self.scaled_img = pg.transform.scale(self.img, (94*scale, 74*scale))

        self.slot_cell_img = pg.image.load("slot-cell.png").convert_alpha()
        self.scaled_cell_img = pg.transform.scale(self.slot_cell_img, (36*scale, 24*scale))
        
        #setup table data
        self.pos = pos
        self.srf = pg.Surface((94*scale, 37*scale)).convert_alpha()

        #init prior list of big cards
        prior = [
            [0,0], [3, 0], [4, 0], [1,0],
            [0,1], [3, 1], [4, 1], [1,1],
            [0,5], [3, 5], [4, 5], [1,5],
            [0,2], [3, 2], [4, 2], [1,2]
        ]
        self.cards = []
        big_cards = pg.image.load("big-card-sheet.png").convert_alpha()
        for pos in prior:
            init_card = pg.Surface((18, 24)).convert_alpha()
            init_card.blit(big_cards, (0,0), (pos[0]*18, pos[1]*24, 18, 24))
            add_card = pg.transform.scale(init_card, (18*scale, 24*scale))
            self.cards.append(add_card)

        #setup slot data
        self.slot_list = []
        for x in range(4):
            slot_srf = pg.Surface((18*scale, 24*scale)).convert_alpha()
            slot_srf.blit(self.scaled_cell_img, (0,0), (0, 0, 18*scale, 24*scale))
            slot_pos = [(89 - (18*(x+1)) - 4*x )*scale, int((37-24)/2)*scale]

            new_x = slot_pos[0] + self.pos[0]
            new_y = slot_pos[1] + self.pos[1]
            slot_rect = pg.Rect(new_x, new_y, 18*scale, 24*scale)
            #add empty_img, then pos, then card_img (-1 is none)

            card = [slot_srf, slot_pos, -1, slot_rect]
            self.slot_list.append(card)
        # white or dark frame
        self.active_state = False

        # float_card data ---not in use yet
        self.card_in_hover = 17
        self.card_in_use = False

        # get data of all cards in slot-cells
        self.data_list = []
        for card in self.slot_list:
            self.data_list.append(card[2])
    def update_data(self):
        self.data_list = []
        for card in self.slot_list:
            self.data_list.append(card[2])

    def mouse_collide(self, rect):
        mos_pos = pg.mouse.get_pos()
        return rect.collidepoint(mos_pos)

    def float_card(self, rect, index, scr): #not used yet
        mos_pos = pg.mouse.get_pos()
        dx = mos_pos[0] - int(rect.width)/2
        dy = mos_pos[1] - int(rect.height)/2

        pressed = pg.mouse.get_pressed()[0]

        if rect.collidepoint(mos_pos) and pressed:
            if not self.card_in_use:
                self.card_in_hover = index
            self.card_in_use = True
        if pressed:
            try:
                scr.blit(self.cards[card_in_hover], (dx, dy))
            except: 
                self.card_in_use = False
        if not pressed:
            card_in_hover = 17
            self.card_in_use = False
    
    def card_func(self, int_val, card_in_use, scr):
        # if 3rd arg is -1, use default img
        # if hover, use white default, else, dark
        #print(card_in_use)
        pressed_list = pg.mouse.get_pressed()
        for card in self.slot_list:
            blit_img = card[0]
            if self.mouse_collide(card[3]) and card_in_use and not pressed_list[0]:
                card[2] = int_val
            elif self.mouse_collide(card[3]) and not card_in_use and pressed_list[2]:
                card[2] = -1
                #self.float_card(card[3], int_val, scr)
            if card[2] != -1:
                blit_img = self.cards[card[2]]
            self.update_data()
            self.srf.blit(blit_img, card[1])

    def blit(self, scr, int_val, card_in_use):
        #print(self.data_list)
        if self.active_state:
            self.srf.blit(self.scaled_img, (0,0), (0, 0, 94*scale, 37*scale))
        else:
            self.srf.blit(self.scaled_img, (0,0), (0, 37*scale, 94*scale, 37*scale))
        self.card_func(int_val, card_in_use, scr)
        scr.blit(self.srf, self.pos)
        return self.data_list

class button:
    def __init__(self, pos, sheet):
        self.sheet = sheet #spritesheet
        rect = self.sheet.get_rect()
        self.rect = pg.Rect(pos[0], pos[1], rect.width*scale, rect.height/2*scale)
        self.sheet = pg.transform.scale(self.sheet, (rect.width*scale, int(rect.height)*scale))

        self.blit_srf = pg.Surface((rect.width * scale, rect.height/2 *scale)) # img to blit
        self.default_img = pg.Surface((rect.width * scale, rect.height/2 * scale)) # non hover
        self.pressed_img = pg.Surface((rect.width * scale, rect.height/2 * scale)) # mouse hover

        self.default_img.blit(self.sheet, (0,0), (0, 0, rect.width*scale, rect.height/2*scale))
        self.pressed_img.blit(self.sheet, (0,0), (0, rect.height/2*scale, rect.width*scale, rect.height/2*scale))

        self.mouse_hover = False
        self.clicked = False
    def update(self, scr):
        mos_pos = pg.mouse.get_pos()
        pressed = pg.mouse.get_pressed()[0]
        img = self.default_img
        #print(f"{self.rect} : {mos_pos}")

        if self.rect.collidepoint(mos_pos):
            self.hover = True
        else:
            self.hover = False
        
        if self.hover:
            img = self.pressed_img
        elif not self.hover:
            img = self.default_img
        self.blit_srf.blit(img, (0,0))
        scr.blit(self.blit_srf, self.rect)