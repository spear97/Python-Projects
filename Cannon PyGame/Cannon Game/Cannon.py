#Import Pygame Module
import pygame

class Cannon:

    #Constructor
    def __init__(self, _img, x, y):
        self.image = _img
        self.x = x
        self.y = y
        self.rect = pygame.Rect((x, y), (self.image.get_width(), self.image.get_height()))

    #Move Cannon Right
    def moveRight(self, win, _vel):
        if self.rect.midright[0] < (win.get_width() - 14):
            return self.x + _vel
        else:
            return self.x

    #Move Cannon Left
    def moveLeft(self, win, _vel):
        if self.rect.midleft[0] > ((win.get_width() - win.get_width()) + 10):
            return self.x - _vel
        else:
            return self.x

    #Get the Position of the CannonBall
    def getPosition(self):
        return (self.x, self.y)

    #Get the Resolution of the CannonBall's Image
    def getResolution(self):
        return (self.image.get_width(), self.image.get_height())