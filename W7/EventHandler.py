import pygame as pg
class EventHandler:
    def __init__(self, window) -> None:
        self.window = window
        
    def listen(self, events) -> None:
        left, right = 0, 0
        
        #Event capture
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_LEFT, pg.K_a):
                    print("Left")
                elif event.key in (pg.K_RIGHT, pg.K_d):
                    print("Right")
            elif event.type == pg.MOUSEMOTION:
                x, y = event.pos
                print(f"x: {x}\ty: {y}")
                