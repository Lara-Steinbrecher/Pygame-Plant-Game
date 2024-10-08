import pygame

class Planta():
    def __init__(self, x, y):
        self.plant_stages = [
            pygame.image.load("assets//images//maceta.png").convert_alpha(),
            pygame.image.load("assets//images//etapa1_planta.png").convert_alpha(),
            pygame.image.load("assets//images//etapa2_planta.png").convert_alpha(),
            pygame.image.load("assets//images//etapa3_planta.png").convert_alpha(),
            pygame.image.load("assets//images//etapa4_planta.png").convert_alpha(),
            pygame.image.load("assets//images//etapa5_planta.png").convert_alpha(),
            pygame.image.load("assets//images//etapa6_planta.png").convert_alpha()
        ]
        self.index = 0
        self.imagen = self.plant_stages[self.index]
        self.mask = pygame.mask.from_surface(self.imagen)
        self.rect = self.imagen.get_rect(center=(x, y))

    def draw(self, screen):
        self.screen = screen
        self.imagen = self.plant_stages[self.index]
        self.screen.blit(self.imagen, self.rect)

    def change_stage(self):
        self.index += 1