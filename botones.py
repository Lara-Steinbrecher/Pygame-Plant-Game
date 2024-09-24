import pygame
import CONSTANTES as c

class Icon():
    def __init__(self, image, x ,y):
        self.image = image
        self.shape = image.get_rect()
        #pygame.Rect.update(self.shape, 0, 0, 35,150)
        #self.shape = pygame.Rect(0, 0, 50, 50) # Crea un rectangulo en cierta coordenada (x, y) de tantos pixeles (20, 20)
        self.shape.center = (x, y) # segun la coord que le demos se mueve inmediatamente ahi  
    

    def draw(self, screen):
        screen.blit(self.image, self.shape) # Me permite dibujar la imagen en pantalla
        pygame.draw.rect(screen, [0,200,0], self.shape, 2 ) #color RGB, el 1 es el ancho del contorno si es que tiene

class Boton():
    def __init__(self, on, off, x ,y):
        self.on = on
        self.on_shape = on.get_rect()
        self.off = off
        self.off_shape = off.get_rect()
        #pygame.Rect.update(self.shape, 0, 0, 35,150)
        #self.shape = pygame.Rect(0, 0, 50, 50) # Crea un rectangulo en cierta coordenada (x, y) de tantos pixeles (20, 20)
        self.off_shape.center = (x, y) # segun la coord que le demos se mueve inmediatamente ahi  
        self.on_shape.center = (x, y)

        self.need = 100

    def draw(self, var, screen):

        if var < 0:
            screen.blit(self.on, self.on_shape) # Me permite dibujar la imagen en pantalla
            pygame.draw.rect(screen, [0,200,0], self.on_shape, 2 ) #color RGB, el 1 es el ancho del contorno si es que tiene
        elif var > 0:
            screen.blit(self.off, self.off_shape) # Me permite dibujar la imagen en pantalla
            pygame.draw.rect(screen, [0,200,0], self.off_shape, 2 ) #color RGB, el 1 es el ancho del contorno si es que tiene


class Mood():
    def __init__(self, bad, meh, good, x, y):
        self.bad = bad
        self.bad_shape = bad.get_rect()
        self.meh = meh
        self.meh_shape = meh.get_rect()
        self.good = good
        self.good_shape = good.get_rect()

        self.bad_shape.center = (x, y)
        self.meh_shape.center = (x, y)
        self.good_shape.center = (x, y)
    
    def draw (self, screen, vida):
        if vida > 75:
            screen.blit(self.good, self.good_shape)
        if vida < 75 and vida > 25:
            screen.blit(self.meh, self.meh_shape)
        if vida < 25:
            screen.blit(self.bad, self.bad_shape)

class Time_skip():
    def __init__(self, image, x ,y):
        self.image = image
        self.image_shape = image.get_rect()
        self.image_shape.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.image_shape) # Me permite dibujar la imagen en pantalla
        pygame.draw.rect(screen, [0,200,0], self.image_shape, 2 ) #color RGB, el 1 es el ancho del contorno si es que tiene

      