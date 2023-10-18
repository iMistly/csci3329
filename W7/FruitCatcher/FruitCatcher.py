from Bucket import *
from Strawberry import *
from CONSTANTS import *
import pygame as pg
from EventHandler import *

pg.init()

disp = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
try:
    bg = pg.image.load(SCREEN_BG)
    bg = pg.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    disp.blit(bg, (0,0))
except:
    disp.fill(SCREEN_BGCOLOR)

mainClock = pg.time.Clock()
handler = EventHandler(disp)

while True:
    handler.listen(pg.event.get())

    handler.play()
    
    mainClock.tick(FPS)
    pg.display.update()