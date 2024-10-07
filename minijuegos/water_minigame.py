import pygame
import CONSTANTES as c
import random
from objects.object import Object
from menu_music import choque_obj, saltito

class Water_Minigame():
    def __init__(self, screen, font, escale_img):
        self.screen = screen
        self.font = font
        self.escale_img = escale_img
        self.jump = False
        # Digamos
        self.ground = 273
        print ('ground:', self.ground)
        self.person_X = 150
        print ('person_x:', self.person_X)
        self.person_Y = self.ground
        self.person_Y_speed = 0

        ### Draw the background ###
        self.background = Object("assets//images//background_minijuegoagua.png",c.ANCHO // 2, c.ALTO // 2)

        ### Draw the person ###
        self.person = Object("assets//images//regaderaminigameagua.png", 100, 275)
        
        ### Draw the obstacles ###
        # obstacle_image_unescaled = pygame.image.load("assets//images//obstacle.jpg")
        # obstacle_image = escale_img(obstacle_image_unescaled, 0.125)
        self.obstacle1 = Object("assets//images//rastrillominigameagua.png", random.randint(280, 320), 332)
        self.obstacle2 = Object("assets//images//abeja.png", random.randint(450,480), 275)

        self.tap = Object("assets//images//macetaminigameagua.png", 550, 333)

    def run (self):
        self.person.rect.topleft = (self.person_X, self.person_Y)

        self.background.draw(self.screen)
        self.screen.blit(self.person.imagen, (self.person_X,self.person_Y))
        self.tap.draw(self.screen)
        self.obstacle1.draw(self.screen)
        self.obstacle2.draw(self.screen)

        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_LEFT]:
            self.person_X -= c.PERSON_SPEED
        if self.keys[pygame.K_RIGHT]:
            self.person_X += c.PERSON_SPEED

        if self.jump == False:
            if self.keys[pygame.K_SPACE]:
                saltito()
                self.jump = True
                self.person_Y_speed = -c.PERSON_JUMP

        if self.jump:
            self.person_Y += self.person_Y_speed
            self.person_Y_speed += c.PERSON_GRAVITY 

            if self.person_Y >= self.ground:
                self.person_Y = self.ground
                self.jump = False
                self.person_Y_speed = 0

        # Colisión con bordes
        #   Lado izquierdo
        if self.person_X < (c.ANCHO // 2 - self.background.rect.width // 2):
            self.person_X = c.ANCHO // 2 - self.background.rect.width // 2
        #   Lado derecho
        if self.person_X > (c.ANCHO // 2 + self.background.rect.width // 2 - 30):
            self.person_X = c.ANCHO // 2 + self.background.rect.width // 2 - 30

        # Colisión de personaje con obstaculo
        if self.person.check_collision(self.obstacle1.rect, self.obstacle1.mask) or self.person.check_collision(self.obstacle2.rect, self.obstacle2.mask):
            self.person_X = c.PERSON_X
            choque_obj()
        
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_ESCAPE]:
            return 2
        
        if self.person.rect.colliderect(self.tap.rect):
            print('collide')
            return 1
        else:
            return 0
        