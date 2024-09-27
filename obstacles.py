import pygame
import CONSTANTES as c

class obstacle():
    def __init__(self, image, x, y):
        self.image = image
        self.shape = image.get_rect()
        self.shape.center = (x, y)
    

    def draw(self):
        screen.blit(self.image, self.shape)