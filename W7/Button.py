import pygame as pg

class Button:
    def __init__(self, window, x, y, width, height) -> None:
        self.window = window
        self.rect = pg.Rect(x, y, width, height)
        self.colorIdle = (150, 150, 150)
        self.colorHover = (200, 200, 200)
        self.colorClick = (225, 0, 225)
        self.state = 'default'
    
    def draw(self):
        if(self.state == 'default'):
            pg.draw.rect(self.window, self.colorIdle, self.rect)
        elif(self.state == 'hover'):
            pg.draw.rect(self.window, self.colorHover, self.rect)
        elif(self.state == 'click'):
            pg.draw.rect(self.window, self.colorClick, self.rect)
            
    def eventResponse(self, eventObject):
        collision = self.rect.collidepoint(pg.mouse.get_pos())
                
        for event in eventObject:
            if (event.type == pg.MOUSEBUTTONDOWN or pg.mouse.get_pressed()[0]) and collision:
                self.state = 'click'
            elif event.type == pg.MOUSEBUTTONUP and collision:
                self.state = 'hover'
            elif collision:
                self.state = 'hover'
            else:
                self.state = 'default'