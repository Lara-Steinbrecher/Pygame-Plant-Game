import pygame
import CONSTANTES as c
import random

class Water_Minigame():
    def __init__(self, screen, font, escale_img):
        self.screen = screen
        self.font = font
        self.escale_img = escale_img
        self.jump = False
        # Digamos
        self.ground = 236 + 150 - 60
        print ('ground:', self.ground)
        self.person_X = 200
        print ('person_x:', self.person_X)
        self.person_Y = self.ground
        self.person_Y_speed = 0

        ### Draw the background ###

        # background_image_unescaled = pygame.image.load("assets//images//waterMiniGameBackground.jpg")
        # background_image = escale_img(background_image_unescaled, 0.7)
        # background_rect = background_image.get_rect(center=(c.ANCHO // 2, c.ALTO // 2))
        self.background = pygame.Surface((450,300))
        self.background.fill('black')
        self.background_rect = self.background.get_rect(center = (c.ANCHO // 2, c.ALTO // 2))


        ### Draw the person ###
        # person_image_unescaled = pygame.image.load("assets//images//person.jpg")
        # person_image = escale_img(person_image_unescaled, 0.125)
        # person_rect = person_image_unescaled.get_rect(center=(person_X, person_Y))
        self.person = pygame.Surface((30,60))
        self.person.fill('blue')
        self.person_rect = self.person.get_rect(center = (200, 356))
        print ('background', self.background_rect)
        
        ### Draw the obstacles ###
        # obstacle_image_unescaled = pygame.image.load("assets//images//obstacle.jpg")
        # obstacle_image = escale_img(obstacle_image_unescaled, 0.125)
        self.obstacle1 = pygame.Surface((30,30))
        self.obstacle1.fill('green')
        self.obstacle2 = pygame.Surface((30,30))
        self.obstacle2.fill('green')
        self.obstacle3 = pygame.Surface((30,30))
        self.obstacle3.fill('green')
        self.obstacle_rect1 = self.obstacle1.get_rect(center = (random.randrange(250, 300), 356))
        self.obstacle_rect2 = self.obstacle2.get_rect(center = (random.randrange(350, 400), 356))
        self.obstacle_rect3 = self.obstacle3.get_rect(center = (random.randrange(450, 500), 356))
        # obstacle1 = Obstacle(obstacle_image, random.randrange(100, 200),ground)
        # obstacle2 = Obstacle(obstacle_image, random.randrange(250, 350),ground)
        # obstacle3 = Obstacle(obstacle_image, random.randrange(400, 500), ground)
        

        ### Draw the tap ###
        # tap_image_unescaled = pygame.image.load("assets//images//tap.jpg")
        # tap_image = escale_img(tap_image_unescaled, 0.125)
        # tap_rect = tap_image.get_rect(center=(c.TAP_X, ground))
        self.tap = pygame.Surface((30,60))
        self.tap.fill('purple')
        self.tap_rect = self.tap.get_rect(center = (550, 356))

    def run (self):
        self.person_rect.topleft = (self.person_X, self.person_Y)
        
        self.screen.blit(self.background, self.background_rect)

        self.screen.blit(self.person, (self.person_X,self.person_Y))

        self.screen.blit(self.tap, self.tap_rect)

        self.screen.blit(self.obstacle1, self.obstacle_rect1)
        self.screen.blit(self.obstacle2, self.obstacle_rect2)
        self.screen.blit(self.obstacle3, self.obstacle_rect3)
        # obstacle1.draw(screen)
        # obstacle2.draw(screen)
        # obstacle3.draw(screen)

        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_LEFT]:
            self.person_X -= c.PERSON_SPEED
        if self.keys[pygame.K_RIGHT]:
            self.person_X += c.PERSON_SPEED

        if self.jump == False:
            if self.keys[pygame.K_SPACE]:
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
        if self.person_X < (c.ANCHO // 2 - self.background_rect.width // 2):
            self.person_X = c.ANCHO // 2 - self.background_rect.width // 2
        #   Lado derecho
        if self.person_X > (c.ANCHO // 2 + self.background_rect.width // 2 - 30):
            self.person_X = c.ANCHO // 2 + self.background_rect.width // 2 - 30

        # Colisión de personaje con obstaculo
        if self.person_rect.colliderect(self.obstacle_rect1) or self.person_rect.colliderect(self.obstacle_rect2) or self.person_rect.colliderect(self.obstacle_rect3):
            self.person_X = c.PERSON_X

        if self.person_rect.colliderect(self.tap_rect):
            print('collide')
            return 1
        else:
            return 0