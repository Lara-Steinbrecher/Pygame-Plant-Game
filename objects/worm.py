import pygame
import random

class Worm():
    def __init__(self, pot_rect):
        self.alignment = random.randint(0,1)
        if self.alignment == 0:
            self.body = pygame.Surface((20,40))
            # Los dos rect de abajo los coloca tiene como máximo/mínimo los bordes del pot
            # Si queres que haya más separación cambialos de +-10/20 a +-20/40
            self.rect = self.body.get_rect(center=(random.randint(pot_rect.left + 10, pot_rect.right - 10) , random.randint(pot_rect.top +  20, pot_rect.bottom - 20)))
        else:
            self.body = pygame.Surface((40,20))
            self.rect = self.body.get_rect(center=(random.randint(pot_rect.left + 20, pot_rect.right - 20), random.randint(pot_rect.top + 10, pot_rect.bottom - 10)))
        
        self.body.fill('green')