import pygame as pg
from Button import *

pg.init()

mainDisp = pg.display.set_mode((800, 600))
mainDisp.fill((255,100,100))

# rect = pg.rect.Rect(10, 10, 100, 50)
# pg.draw.rect(mainDisp, (200, 200, 200), rect)

button1 = Button(mainDisp, 50, 50, 100, 50)

mainClock = pg.time.Clock()

while(True):
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    button1.eventResponse(events)
    button1.draw()
    mainClock.tick(60)
    pg.display.update()