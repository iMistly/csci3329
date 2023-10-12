import pygame as pg
from EventHandler import *

pg.init()

disp = pg.display.set_mode((720, 480))
disp.fill((200,200,200))

mainClock = pg.time.Clock()

handler = EventHandler(disp)

while True:
    handler.listen(pg.event.get())
    
    mainClock.tick(60)
    pg.display.update()