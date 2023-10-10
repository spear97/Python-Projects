#Import Pygame Module
import pygame

class CannonBall:

    #Constructor
    def __init__(self, _img, x, y):
        self.image = _img
        self.x = x
        self.y = y
        self.rect = pygame.Rect((x, y), (self.image.get_width(), self.image.get_height()))

    #Move the CannonBall Up
    def moveUp(self, _vel):
        return self.y - _vel

    #Get the Position of the CannonBall
    def getPosition(self):
        return (self.x, self.y)

    #Get the Resolution of the CannonBall's Image
    def getResolution(self):
        return (self.image.get_width(), self.image.get_height())