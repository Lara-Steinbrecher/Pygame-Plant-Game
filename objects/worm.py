import pygame
import random

class Worm():
    def __init__(self, pot_rect):
        self.alignment = random.randint(0,1)
        self.pot_rect = pot_rect

        self.worm_image = [
            pygame.image.load("assets//images//Minijuego-tierra-gusano-1.png"),
            pygame.image.load("assets//images//Minijuego-tierra-gusano-2.png"),
            pygame.image.load("assets//images//Minijuego-tierra-gusano-3.png"),
            pygame.image.load("assets//images//Minijuego-tierra-gusano-4.png"),
            pygame.image.load("assets//images//Minijuego-tierra-gusano-5.png"),
            pygame.image.load("assets//images//Minijuego-tierra-gusano-6.png"),
        ]

        for i in range(len(self.worm_image)):
            self.worm_image[i] = pygame.transform.scale_by(self.worm_image[i],0.5)

        if self.alignment == 0:
            self.body = self.worm_image[random.randint(0,5)]
            # Los dos rect de abajo los coloca tiene como máximo/mínimo los bordes del pot
            # Si queres que haya más separación cambialos de +-10/20 a +-20/40
            self.rect = self.body.get_rect(center=(random.randint(self.pot_rect.left + self.pot_rect.width // 2, self.pot_rect.right - self.pot_rect.width // 2) , random.randint(self.pot_rect.top +  self.pot_rect.height // 2, self.pot_rect.bottom - self.pot_rect.height // 2)))
            self.mask = pygame.mask.from_surface(self.body)

        else:
            self.body = self.worm_image[random.randint(0,5)]
            self.body = pygame.transform.rotate(self.body,90)
            self.rect = self.body.get_rect(center=(random.randint(pot_rect.left + pot_rect.width // 2, pot_rect.right - pot_rect.width // 2), random.randint(pot_rect.top + pot_rect.height // 2, pot_rect.bottom - pot_rect.height // 2)))
            self.mask = pygame.mask.from_surface(self.body)

    def check_collision(self, pos, mask):
        self.pos_other = pos
        self.mask_other = mask
        self.pos_difference = (self.pos_other[0] - self.rect.x, self.pos_other[1] - self.rect.y)
        if self.mask.overlap(self.mask_other, self.pos_difference):
            return 1