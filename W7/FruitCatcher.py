import pygame as pg

pg.init()

disp = pg.display.set_mode((720, 480))
disp.fill((200,200,200))

mainClock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    
    mainClock.tick(60)
    pg.display.update()