import pygame as pg
import sys
from random import randint
#追加2
import tkinter as tk
import tkinter.messagebox as tkm

key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
}

def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate



def main():
    #1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #5
    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)
    #6
    vx, vy = +1, +1

    #追加1
    bomb_sfc2 = pg.Surface((20, 20))
    bomb_sfc2.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc2, (255, 128, 0), (10, 10), 10)
    bomb_rct2 = bomb_sfc.get_rect()
    bomb_rct2.centerx = randint(0, scrn_rct.width)
    bomb_rct2.centery = randint(0, scrn_rct.height)
    #6
    vx2, vy2 = +1, +1


    clock = pg.time.Clock() #1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) #2
        
        for event in pg.event.get(): #2
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:    tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:  tori_rct.centery += 1
        if key_states[pg.K_LEFT]:  tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]: 
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]: 
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1            
        scrn_sfc.blit(tori_sfc, tori_rct) #3

        #7
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy) #6
        scrn_sfc.blit(bomb_sfc, bomb_rct) #5

        if tori_rct.colliderect(bomb_rct):
            return tkm.showwarning("爆発", "ゲームオーバー！")#追加2

        #追加1
        yoko, tate = check_bound(bomb_rct2, scrn_rct)
        vx2 *= yoko
        vy2 *= tate
        bomb_rct2.move_ip(vx2, vy2) #6
        scrn_sfc.blit(bomb_sfc2, bomb_rct2) #5

        #追加3
        if tori_rct.colliderect(bomb_rct2):
            tori_sfc = pg.image.load("fig/5.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)

        pg.display.update() #2
        clock.tick(1000)


   


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()