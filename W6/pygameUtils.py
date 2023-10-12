import pygame as pg

class EventHandler:
    def __init__(self, display) -> None:
        self.queueOfEvents = []
        self.display = display
        self.images = []
    def loadImages(self, img):
        self.images.append(img)
    
    def listen(self, events):
        self.queueOfEvents = events
        for event in self.queueOfEvents:
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.MOUSEMOTION:
                self.display.fill((75,100,170))
                self.display.blit(self.images[0], (pg.mouse.get_pos()[0] - self.images[0].get_width()/2, pg.mouse.get_pos()[1] - self.images[0].get_height()/2))
    
    
    def mouseEvent(self):
        pass
    
    def keyEvent(self):
        pass