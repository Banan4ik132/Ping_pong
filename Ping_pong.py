import pygame

class Board(pygame.Rect):
    def __init__(self, x , y, widht, height, color, speed, name= "player"):
        super().__init__(x, y, widht, height)
        self.COLOR = color
        self.SPEED = speed
        self.NAME = name 
        self.SCORE = 0
        self.MOVE = {"UP": False, "DOWN": False}

    def move(self, window):
        if self.MOVE["UP"]:
            self.y -= self.SPEED
        elif self.MOVE["DOWN"]:
            self.y += self.SPEED
        pygame.draw.rect(window, self.COLOR, self)