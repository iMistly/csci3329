import pygame as pg
import random
from CONSTANTS import *
class Berry:
    def __init__(self) -> None:
        self.image = pg.image.load("strawberry.png")
        self.image = pg.transform.scale(self.image, STRAWBERRY_SIZE)
        self.rect = self.image.get_rect()
        self.coords = (random.randint(0, SCREEN_WIDTH-self.rect.width), -(self.rect.height/2))
        self.dropSpeed = DROP_SPEED_INITIAL

    def draw(self, window) -> None:
        window.blit(self.image, self.coords)

    def update(self) -> None:
        self.coords = (self.coords[0], self.coords[1] + self.dropSpeed)
        self.rect.x = self.coords[0]
        self.rect.y = self.coords[1]

    def reload(self) -> None:
        self.coords = (random.randint(0, SCREEN_WIDTH-self.rect.width), -(self.rect.height/2))
