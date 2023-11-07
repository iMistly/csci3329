import pygame as pg
import Strawberry
from CONSTANTS import *
class Bucket(Strawberry.Berry):
    def __init__(self) -> None:
        super().__init__()
        self.image = pg.image.load("bucket.png")
        self.image = pg.transform.scale(self.image, BUCKET_SIZE)
        self.rect = self.image.get_rect()
        self.coords = (SCREEN_WIDTH/2, SCREEN_HEIGHT-self.rect.height)

    def update(self, mousePos) -> None:
        self.coords = (mousePos[0] - self.rect.width/2, self.coords[1])
        self.rect.x = self.coords[0]
        self.rect.y = self.coords[1]