#use for 
#fix deck card mechanism---done
#change card sheet from 36 cards to 16
import pygame as pg

scale = 4

def dead_cntr (scr, dim):
    x = abs(int((scr.get_width() - dim[0])/2))
    y = abs(int((scr.get_height() - dim[1])/2))
    return [x, y]


class card_obj(pg.sprite.Sprite):
    def __init__(self, rect_data, kindOf, srf, deckPos, screen):
        pg.sprite.Sprite.__init__(self)
        self.rect = rect_data 
        self.img = kindOf #what color and symbol
        flipped_img = pg.image.load("flipped-card.png").convert_alpha()
        self.flipped_img = pg.transform.scale(flipped_img, (14*scale, 17*scale))
        self.blit_img = self.flipped_img
        self.blit_srf = screen
        self.screen = screen
        
        self.hint_active = False
        self.hover = False #tracks if mouse hovers over card
        self.in_use = False #sets if the deck shows an empty-card or a flipped one

        self.deckPos = deckPos

        new_x = self.rect.x + self.deckPos[0]
        new_y = self.rect.y + self.deckPos[1]
        self.apparent_rect = pg.Rect(new_x, new_y, self.rect.w, self.rect.h)
        hover_y = self.apparent_rect.y - 6*scale
        self.hover_rect = pg.Rect(self.apparent_rect.x, hover_y, self.rect.w, self.rect.h)
        #print(self.deckPos)
        #print(self.apparent_rect)
        #print(self.rect)
        #print(self.hover_rect)

        # the card objs will be updated through a sprite group
    def mouse_track(self):
        mos_pos = pg.mouse.get_pos()
        #pg.draw.rect(self.blit_srf, (0, 255, 0), self.apparent_rect, 2)

        if self.apparent_rect.collidepoint(mos_pos):
            self.hover = True
        else:
            self.hover = False
        #print(self.hover)
        #print(mos_pos)
        #rect data is relative to the its surface, problem with 
        #print(self.apparent_rect)
    
    def update(self):
        self.mouse_track()
        self.blit_srf.blit(self.blit_img, self.apparent_rect)

        if self.hover:            
            self.blit_srf.blit(self.img, self.hover_rect)
        #self.blit_srf.blit(self.blit_img, self.rect)

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
            #slot_pos = dead_cntr(self.srf, [18*scale, 24*scale])
            slot_pos = [(89 - (18*(x+1)) - 4*x )*scale, int((37-24)/2)*scale]
            #add empty_img, then pos, then card_img (-1 is none)

            card = [slot_srf, slot_pos, -1]
            self.slot_list.append(card)

        self.active_state = False
    def hover(self, rect):
        mos_pos = pg.mouse.get_pos()
        return rect.collidepoint(mos_pos)
    
    def card_func(self):
        # if 3rd arg is -1, use default img
        # if hover, use white default, else, dark
        for card in self.slot_list:
            blit_img = card[0]
            if card[2] != -1:
                blit_img = self.cards[card[2]]
            self.srf.blit(blit_img, card[1])
            
    def blit(self, scr):
        if self.active_state:
            self.srf.blit(self.scaled_img, (0,0), (0, 0, 94*scale, 37*scale))
        else:
            self.srf.blit(self.scaled_img, (0,0), (0, 37*scale, 94*scale, 37*scale))
        self.card_func()
        scr.blit(self.srf, self.pos)
