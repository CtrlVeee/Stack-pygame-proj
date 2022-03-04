
import pygame as pg

pg.init()
scr_w = 720
scr_h = 576
scr = pg.display.set_mode((scr_w, scr_h))

fps = 30
clock = pg.time.Clock()

bg_color = (70, 70, 70)
def main():
    loop = True
    while loop:
        scr.fill(bg_color)
        scr.blit
        pg.display.update()

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                loop = False
                break 
            elif ev.type == pg.KEYDOWN:
                pass
        clock.tick(fps)
        
main()