import pygame as pg
from pygame.locals import *
import sys
import random as rd


def main():

    #自分
    SCR_WIDTH, SCR_HEIGHT = 1600, 900#ウィンドウのサイズ設定
    scrn_sfc = pg.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pg.display.set_caption("PACMAN")
    (x, y) = (0, 400)
    sfc1 = pg.image.load("pngwing.com.png").convert_alpha()
    rct1 = sfc1.get_rect()
    sfc1 = pg.transform.rotozoom(sfc1,0,0.07)
    

    enemy1 = pg.image.load("pngwing.com2.png").convert_alpha()#敵1
    enemy_rect1 = enemy1.get_rect()
    enemy1 = pg.transform.rotozoom(enemy1,0,0.07)
    vx = vy = 7
    clock = pg.time.Clock()

    enemy2 = pg.image.load("pngwing.com3.png").convert_alpha()#敵2
    enemy_rect2 = enemy2.get_rect()
    enemy2 = pg.transform.rotozoom(enemy2,0,0.13)

    vx2 = vy2 = 7
    clock = pg.time.Clock()

    while True:
        #敵1
        clock.tick(60)
        enemy_rect1.move_ip(vx, vy)
        if enemy_rect1.left < 0 or enemy_rect1.right > SCR_WIDTH+800:
            vx = -vx
        if enemy_rect1.top < 0 or enemy_rect1.bottom > SCR_HEIGHT:
            vy = -vy
        pg.display.update()
        pg.time.wait(40)

        #敵2
        clock.tick(60)
        enemy_rect2.move_ip(vx2, vy2)
        if enemy_rect2.left < 0 or enemy_rect2.right > SCR_WIDTH:
            vx2 = -vx2
        if enemy_rect2.top < 0 or enemy_rect2.bottom > SCR_HEIGHT+500
            vy2 = -vy2
        pg.display.update()
        pg.time.wait(40)


        scrn_sfc.fill((255, 255, 255))
        scrn_sfc.blit(sfc1, (x, y))
        scrn_sfc.blit(enemy1, enemy_rect1)#敵1

        scrn_sfc.blit(enemy2, enemy_rect2)#敵2



        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_a:
                    x -= 50
                    y += 0
                if event.key == K_d:
                    x += 50
                    y += 0
                if event.key == K_w:
                    x += 0
                    y -= 50
                if event.key == K_s:
                    x += 0
                    y += 50
                if event.key == K_0:
                    (x, y) = (0, 400)
            if rct1.right > SCR_WIDTH:#端まで行ったら終了
                pg.quit()
                sys.exit()
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()

        #for event in pg.event.get():
        #    if event.type == MOUSEMOTION:
        #       x, y = event.pos
        #        x -= int(sfc1.get_width()/2)
        #        y -= int(sfc1.get_height()/2)
        

if __name__ == "__main__":
    pg.init()
    main()