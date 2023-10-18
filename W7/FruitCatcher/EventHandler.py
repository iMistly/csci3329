import pygame as pg
from CONSTANTS import *
from Strawberry import *
from Bucket import *

class EventHandler:
    def __init__(self, window) -> None:
        self.window = window
        self.score = 0
        self.bucket = Bucket()
        self.strawberry = Berry()
        self.status = "running"
        
    def listen(self, events) -> None:
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            # elif event.type == pg.KEYDOWN:
            #     if event.key in (pg.K_LEFT, pg.K_a):
            #         print("Left")
            #     elif event.key in (pg.K_RIGHT, pg.K_d):
            #         print("Right")
            elif event.type == pg.MOUSEMOTION:
                self.bucket.update(event.pos)
            elif event.type == pg.MOUSEBUTTONDOWN and self.status == "gameover":
                self.score = 0
                self.strawberry.dropSpeed = DROP_SPEED_INITIAL
                self.status = "running"
    
    def play(self) -> None:
        if self.status == "running":
            self.draw()
            self.checkCatch()
        elif self.status == "gameover":
            self.gameover()
    
    def checkCatch(self):
        if self.bucket.rect.colliderect(self.strawberry.rect):
            self.score += 1
            self.strawberry.dropSpeed += DROP_ACCELERATION
            self.strawberry.reload()
        elif self.strawberry.coords[1] >= SCREEN_HEIGHT:
            self.strawberry.reload()
            self.status = "gameover"

    def displayText(self, inText, coords) -> None:
        #Text Shadow
        if TEXT_SHADOW_ENABLED:
            font = pg.font.SysFont(FONT, FONT_SIZE)
            text = font.render(inText, True, TEXT_SHADOW)
            self.window.blit(text, (coords[0]-text.get_width()/2+TEXT_SHADOW_OFFSET,coords[1]+TEXT_SHADOW_OFFSET))
        #Text
        font = pg.font.SysFont(FONT, FONT_SIZE)
        text = font.render(inText, True, TEXT_COLOR)
        self.window.blit(text, (coords[0]-text.get_width()/2,coords[1]))

    def draw(self) -> None:
        try:
            bg = pg.image.load(SCREEN_BG)
            bg = pg.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.window.blit(bg, (0,0))
        except:
            self.window.fill(SCREEN_BGCOLOR)
        self.strawberry.update()
        self.strawberry.draw(self.window)
        self.bucket.draw(self.window)
        #Score
        self.displayText(f"Score: {self.score}", (SCREEN_WIDTH/2, 0))
        pg.display.update()

    def gameover(self) -> None:
        self.window.fill(SCREEN_BGCOLOR)
        self.displayText("Game Over", (SCREEN_WIDTH/2, SCREEN_HEIGHT/3-FONT_SIZE))
        self.displayText(f"Score: {self.score}", (SCREEN_WIDTH/2, SCREEN_HEIGHT/3))
        self.displayText("Click to play again", (SCREEN_WIDTH/2, SCREEN_HEIGHT/3*2))
        pg.display.update()