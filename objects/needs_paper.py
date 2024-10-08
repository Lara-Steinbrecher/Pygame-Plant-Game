import pygame
import CONSTANTES as c

class Needs_Paper():
    def __init__(self, screen, font, escale_img):
        self.screen = screen
        self.font = pygame.font.Font("assets//fonts//PressStart2P-Regular.ttf", 12)
        self.escale_img = escale_img

        self.background = pygame.image.load("assets//images/post_it.png")
        self.background_rect = self.background.get_rect(center = (c.ANCHO // 2, c.ALTO // 2))

        self.water_bar = Need_Bar(180)
        self.light_bar = Need_Bar(240)
        self.soil_bar = Need_Bar(300)
        self.temp_bar = Need_Bar(360)

    def run(self, water, light, temp, soil):
        self.water_need = water
        self.light_need = light
        self.temp_need = temp
        self.soil_need = soil
        self.screen.blit(self.background, self.background_rect)

        self.needs_text = self.font.render("Necesidades", True, 'black')
        self.agua_text = self.font.render(f"Agua:", True, 'black')
        self.luz_text = self.font.render(f"Luz:", True, 'black')
        self.soil_text = self.font.render(f"Tierra:", True, 'black')
        self.temp_text = self.font.render(f"Temperatura:", True, 'black')

        self.screen.blit(self.needs_text, (c.ANCHO // 2 - 65, c.ALTO // 2 - 160))
        self.screen.blit(self.agua_text, (c.ANCHO // 2 - 100, 150))
        self.screen.blit(self.luz_text, (c.ANCHO // 2 - 100, 210))
        self.screen.blit(self.soil_text, (c.ANCHO // 2 - 100, 270))
        self.screen.blit(self.temp_text, (c.ANCHO // 2 - 100, 330))

        self.water_bar.draw(self.water_need, self.screen, 'blue')
        self.light_bar.draw(self.light_need, self.screen, 'yellow')
        self.soil_bar.draw(self.soil_need, self.screen, 'brown')
        self.temp_bar.draw(self.temp_need, self.screen, 'red')

        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_ESCAPE]:
            return 1
        
class Need_Bar():
    def __init__(self, y):
        self.y = y
        self.background = pygame.Surface((220, 20))
        self.background_rect = self.background.get_rect(center=(c.CENTER[0], self.y))
        self.background.fill('black')

    
    def draw(self, need, screen, color):
        self.screen = screen

        if need <= 0:
            return 0
        
        self.bar = pygame.Surface(((220*(need/100)),18))
        self.bar_rect = self.bar.get_rect(center=(c.CENTER[0],self.y))
        self.bar.fill(color)

        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.bar, self.bar_rect)