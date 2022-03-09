#use for 
import pygame as pg

def dead_cntr (scr, dim):
    x = abs(int((scr.get_width() - dim[0])/2))
    y = abs(int((scr.get_height() - dim[1])/2))
    return (x, y)


class card_obj(pg.sprite.Sprite):
    def __init__(self, rect_data, kindOf, scr):
        pg.sprite.Sprite.__init__(self)
        self.rect = rect_data
        self.img = kindOf #what color and symbol
        self.flipped_img = pg.image.load("flipped-card.png")
        self.blit_srf = scr
        self.hint_active = False
        self.hover = False #tracks if mouse hovers over card
        self.in_use = False #sets if the deck shows an empty-card or a flipped one
        # the card objs will be updated through a sprite group
    def update(self):
        self.blit_srf.blit(self.img, self.rect)
