import pygame
import CONSTANTES as c
import random

class Planta():
    def __init__(self, image):
        self.image = image
        self.shape = image.get_rect()
        #pygame.Rect.update(self.shape, 0, 0, 35,150)
        #self.shape = pygame.Rect(0, 0, 50, 50) # Crea un rectangulo en cierta coordenada (x, y) de tantos pixeles (20, 20)
        self.shape.center = (200,370) # segun la coord que le demos se mueve inmediatamente ahi

    def regar(self, contadorTrueFalse, barra, activador):
        if contadorTrueFalse == True and activador == True :
            randomnum = random.randrange(12, 36)
            barra = barra + randomnum
        elif contadorTrueFalse == False and activador == True:
            randomnum = random.randrange(12, 36)
            barra = barra - randomnum
        return barra

    def salud(vida):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.shape) # Me permite dibujar la imagen en pantalla
        pygame.draw.rect(screen, [0,200,0], self.shape, 2 ) #color RGB, el 1 es el ancho del contorno si es que tiene
