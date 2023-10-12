import pygame as pg
class EventHandler:
    def __init__(self, window) -> None:
        self.window = window
        
    def listen(self, events) -> None:
        keys = pg.key.get_pressed()
        
        #Event capture
        for event in events:
            if event.type == pg.QUIT:
                exit()
        
        #Input capture
        if keys[pg.K_LEFT]:
            print("Left")
        if keys[pg.K_RIGHT]:
            print("Right")
        if pg.mouse.get_focused() and pg.mouse.get_rel() != (0,0):
            print(pg.mouse.get_pos())