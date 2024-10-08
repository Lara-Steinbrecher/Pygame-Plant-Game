import pygame

class Termostato():
    def __init__(self, x, y):
        self.aguja_stages = [
            pygame.image.load("assets//images//degrees//veinticuatro_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//veintitres_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//veintidos_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//veintiuno_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//veinte_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//diecinueve_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//dieciocho_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//diecisiete_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//dieciseis_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//quince_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//catorce_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//trece_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//doce_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//once_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//diez_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//nueve_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//ocho_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//siete_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//seis_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//cinco_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//cuatro_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//tres_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//dos_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//un_grado.png").convert_alpha(),
            pygame.image.load("assets//images//degrees//cero_grados.png").convert_alpha(),
        ]
        self.index = 0
        self.imagen = self.aguja_stages[self.index]
        self.mask = pygame.mask.from_surface(self.imagen)
        self.rect = self.imagen.get_rect(center=(x, y))

    def draw(self, screen):
        self.screen = screen
        self.imagen = self.aguja_stages[self.index]
        self.screen.blit(self.imagen, self.rect)

    def change_stage(self):
        self.index += 1
        if self.index >= 25:
            self.index = 0

    def reset_stage(self):
        self.index = 0
