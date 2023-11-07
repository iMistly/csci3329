import pygame as pg
from pygameUtils import EventHandler

pg.init()

mainDisp = pg.display.set_mode((800, 600))

mainDisp.fill((75,100,110))

gameClock = pg.time.Clock()

myImage = pg.image.load('C:/Users/craft/Desktop/csci3329/W6/wah.png')
mainDisp.blit(myImage, (10, 10))

handler = EventHandler(mainDisp)
handler.loadImages(myImage)

while True:
    handler.listen(pg.event.get())
    
    # gameClock.tick(60)
    
    pg.display.update()