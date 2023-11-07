import pygame as pg

class Button:
    def __init__(self, window, x, y, width, height) -> None:
        self.window = window
        self.rect = pg.Rect(x, y, width, height)
        self.colors = {'default': (150, 150, 150), 
                       'hover': (200, 200, 200), 
                       'click': (138, 180, 248)}
        self.state = 'default'
        self.pressed = False
    
    def draw(self):
        pg.draw.rect(self.window, self.colors[self.state], self.rect)
            
    def eventResponse(self, eventObject):
        collision = self.rect.collidepoint(pg.mouse.get_pos())
                
        for event in eventObject:
            if event.type == pg.MOUSEBUTTONDOWN and collision:
                self.pressed = True
            elif event.type == pg.MOUSEBUTTONUP:
                if collision and self.pressed:
                    print('Do something')
                self.pressed = False
                
        
        if self.pressed:
            self.state = 'click'
        else:
            self.state = 'hover' if collision else 'default'