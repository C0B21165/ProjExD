import pygame as pg

def main():
    pg.display.set_caption("逃げろ！こうかとん")#連取1
    scrn_sfc = pg.display.set_mode((1600, 900))
    bg_sfc = pg.image.load("fig/fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #3
    tori_sfc = pg.image.load("fig/fig/7.jpg")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    clock = pg.time.Clock()

    #2
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        #4
        key_status = pg.key.get_pressed()
        if key_status[pg.K_UP]:    tori_rct.centery -= 1
        if key_status[pg.K_DOWN]:  tori_rct.centery += 1
        if key_status[pg.K_LEFT]:  tori_rct.centerx -= 1
        if key_status[K_RIGHT]:    tori_rct.centerx += 1

        #3
        scrn_sfc.blit(tori_sfc, tori_rct)
        pg.display.update()
        
        clock.tick(1000)






if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()