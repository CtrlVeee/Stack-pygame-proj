#use for 
#fix deck card mechanism
import pygame as pg

scale = 4

def dead_cntr (scr, dim):
    x = abs(int((scr.get_width() - dim[0])/2))
    y = abs(int((scr.get_height() - dim[1])/2))
    return (x, y)


class card_obj(pg.sprite.Sprite):
    def __init__(self, rect_data, kindOf, scr, deckPos):
        pg.sprite.Sprite.__init__(self)
        self.rect = rect_data 
        self.img = kindOf #what color and symbol
        flipped_img = pg.image.load("flipped-card.png").convert_alpha()
        self.flipped_img = pg.transform.scale(flipped_img, (14*scale, 17*scale))
        self.blit_img = self.flipped_img
        self.blit_srf = scr
        
        self.hint_active = False
        self.hover = False #tracks if mouse hovers over card
        self.in_use = False #sets if the deck shows an empty-card or a flipped one

        self.deckPos = deckPos
        #print(self.deckPos)

        # the card objs will be updated through a sprite group
    def mouse_track(self):
        mos_pos = pg.mouse.get_pos()
        pg.draw.rect(self.blit_srf, (0, 255, 0), self.rect, 2)

        new_x = self.rect.x + self.deckPos[0]
        new_y = self.rect.y + self.deckPos[1]
        apparent_rect = pg.Rect(new_x, new_y, self.rect.w, self.rect.h)

        if apparent_rect.collidepoint(mos_pos):
            self.hover = True
        else:
            self.hover = False
        #print(mos_pos)
        #rect data is relative to the its surface, problem with 
        #print(apparent_rect)
    
    def update(self):

        #print(self.rect)
        if self.hover == False:
            self.blit_img = self.flipped_img
        #elif self.hover == True:
        #    self.blit_img = self.img
        self.blit_srf.blit(self.blit_img, self.rect)
        self.mouse_track()
