
import sched
import pygame as pg
from obj import *

pg.init()
#convert all sprites to 4x size
scr_w = 720
scr_h = 576
dimen = (scr_w, scr_h)
scr = pg.display.set_mode((scr_w, scr_h))

fps = 30
clock = pg.time.Clock()


bg_color = pg.Color(23, 17, 26)
def main():
    loop = True
    while loop:
        scr.fill(bg_color)
        scr.blit(cards[6*1], dead_cntr(cards[0], dimen))
        pg.display.update()

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                loop = False
                break 
            elif ev.type == pg.KEYDOWN:
                pass
        clock.tick(fps)
        
main()