import pygame
import CONSTANTES as c
import random
from objects.worm import Worm

class Soil_Minigame():
    def __init__(self, screen, font, escale_img):
        self.screen = screen
        self.font = font
        self.escale_img = escale_img
        self.mouse_pressed = False
        self.min_distance = c.MIN_DISTANCE
        self.distance_flag = False

        self.background = pygame.Surface((450,300))
        self.background.fill('black')
        self.background_rect = self.background.get_rect(center = c.CENTER)
        
        self.pot = pygame.Surface((280,280))
        self.pot.fill('brown')
        self.pot_rect = self.pot.get_rect(center = c.CENTER)

        self.worm_quantity = random.randint (c.WORM_QUANTITY_MIN, c.WORM_QUANTITY_MAX)
        self.worms = []
        for i in range(self.worm_quantity):
            while self.distance_flag == False:
                worm = Worm(self.pot_rect)
                if self.check_distance(worm, self.min_distance) == True:
                    self.distance_flag = True
            self.distance_flag = False
            self.worms.append(worm)
        
    def run(self, mouse_pressed):
        self.mouse_position = pygame.mouse.get_pos()
        self.mouse_pressed = mouse_pressed

        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.pot, self.pot_rect)

        # Si itero en la lista en si, tiene problemas con los fps, si queres probalo, a lo sumo es de mi compu
        for worm in self.worms[:]:
            if self.mouse_pressed == True:
                if worm.rect.collidepoint(self.mouse_position):
                    self.worms.remove(worm)
            self.screen.blit(worm.body,worm.rect)

        if len(self.worms) == 0:
            return 1

    def check_distance(self, created_worm, min_distance):
        for worm in self.worms:
            if created_worm.rect.colliderect(worm.rect.inflate(self.min_distance * 2, self.min_distance * 2)):
                return False
        return True