import pygame
import CONSTANTES as c

class Needs_Paper():
    def __init__(self, screen, font, escale_img):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 18)
        self.escale_img = escale_img

        self.background = pygame.image.load("assets//images/post_it.png")
        self.background_rect = self.background.get_rect(center = (c.ANCHO // 2, c.ALTO // 2))

    def run(self, water, light, temp, soil):
        self.water_need = water
        self.light_need = light
        self.temp_need = temp
        self.soil_need = soil
        self.screen.blit(self.background, self.background_rect)

        self.needs_text = self.font.render("Necesidades", True, 'black')
        self.agua_text = self.font.render(f"Agua: {self.water_need}", True, 'black')
        self.luz_text = self.font.render(f"Luz: {self.light_need}", True, 'black')
        self.soil_text = self.font.render(f"Tierra: {self.soil_need}", True, 'black')
        self.temp_text = self.font.render(f"Temperatura: {self.temp_need}", True, 'black')

        self.screen.blit(self.needs_text, (c.ANCHO // 2 - 45, c.ALTO // 2 - 180))
        self.screen.blit(self.agua_text, (c.ANCHO // 2 - 100, c.ALTO // 2 - 90))
        self.screen.blit(self.luz_text, (c.ANCHO // 2 - 100, c.ALTO // 2 - 70))
        self.screen.blit(self.soil_text, (c.ANCHO // 2 - 100, c.ALTO // 2 - 50))
        self.screen.blit(self.temp_text, (c.ANCHO // 2 - 100, c.ALTO // 2 - 30))

        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_ESCAPE]:
            return 1