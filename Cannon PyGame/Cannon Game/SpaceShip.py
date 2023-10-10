#Import Pygame Module
import pygame

from CannonBall import CannonBall

class SpaceShip:

    #Constructor
    def __init__(self, _img, x, y):
        self.image = _img
        self.x = x
        self.y = y
        self.rect = pygame.Rect((x, y), (self.image.get_width(), self.image.get_height()))

    #Move SpaceShip Down
    def moveDown(self, win, _vel):
         if self.rect.midbottom[1] < (win.get_width() - 14):
            return self.y + _vel 
         else:
            return self.y

    #Move SpaceShip Left
    def moveLeft(self, win, _vel):
        if self.rect.midleft[0] > ((win.get_width() - win.get_width()) + 10):
            return self.x - _vel
        else:
            return self.x

    #Move SpaceShip Right
    def moveRight(self, win, _vel):
        if self.rect.midright[0] < (win.get_width() - 14):
            return self.x + _vel
        else:
            return self.x

    #Get the Position of the SpaceShip
    def getPosition(self):
        return (self.x, self.y)

    #Get the Resolution of the SpaceShip
    def getResolution(self):
        return (self.image.get_width(), self.image.get_height())