import pygame
from objects.object import Object
import CONSTANTES as c
import sys

class Tutorial():
    def __init__(self, screen, background, clock):
        self.clock = clock
        self.background = background
        self.screen = screen
        self.tutorial = Object("assets//images//tutorial.png", c.CENTER[0], c.CENTER[1])
        self.loop = 1

    def run(self):
        while(self.loop):
            self.screen.blit(self.background)
            self.tutorial.draw(self.screen)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.loop = 0

            pygame.display.update()
            self.clock.tick(c.FPS)

    
    

        
