import pygame
import CONSTANTES as c
import random

class Planta():
    def __init__(self, image):
        self.image = image
        self.shape = image.get_rect()
        self.shape.center = (200,370)