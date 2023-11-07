import pygame as pg
from Button import *

pg.init()

mainDisp = pg.display.set_mode((1110, 610))
mainDisp.fill((255,100,100))

# rect = pg.rect.Rect(10, 10, 100, 50)
# pg.draw.rect(mainDisp, (200, 200, 200), rect)

buttonList = []
for i in range(10):
    for j in range(10):
        buttonList.append(Button(mainDisp, 10 + 110 * i, 10 + 60 * j, 100, 50))

mainClock = pg.time.Clock()

while(True):
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    for button in buttonList:
        if button.eventResponse(events):
            print('Button Pressed')
        button.draw()

    mainClock.tick(60)
    pg.display.update()