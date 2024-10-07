import pygame
import CONSTANTES as c
import random
from objects.worm import Worm
from objects.object import Object
from menu_music import aplastar_gusano

class Soil_Minigame():
    def __init__(self, screen, font, escale_img):
        self.screen = screen
        self.font = font
        self.escale_img = escale_img
        self.mouse_pressed = False
        self.min_distance = c.MIN_DISTANCE
        self.distance_flag = False
        
        self.pot = Object("assets//images//minijuegotierrafondo.png", c.ANCHO // 2, c.ALTO // 2)
        self.pot.imagen = pygame.transform.scale(self.pot.imagen, (280,280))
        self.pot.rect = self.pot.imagen.get_rect(center= (c.CENTER))

        self.worm_quantity = random.randint (c.WORM_QUANTITY_MIN, c.WORM_QUANTITY_MAX)
        self.worms = []
        for i in range(self.worm_quantity):
            worm = Worm(self.pot.rect)
            self.worms.append(worm)
        
    def run(self, mouse_pressed, mouse_mask):
        self.mouse_position = pygame.mouse.get_pos()
        self.mouse_pressed = mouse_pressed
        self.mouse_mask = mouse_mask

        self.screen.blit(self.pot.imagen, self.pot.rect)

        # Si itero en la lista en si, tiene problemas con los fps, si queres probalo, a lo sumo es de mi compu
        for worm in self.worms[:]:
            if self.mouse_pressed == True:
                if worm.check_collision(self.mouse_position, self.mouse_mask) == True:
                    aplastar_gusano()
                    self.worms.remove(worm)
            self.screen.blit(worm.body,worm.rect)

        if len(self.worms) == 0:
            return 1
        
        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_ESCAPE]:
            return 2