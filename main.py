import pygame
import CONSTANTES as c
from objects.botones import Time_skip
from game_loop import Game_Loop
from game_over import Game_Over
import sys
from menu_music import menu_music, stop_music

pygame.init() 

class Menu:
    def __init__(self):
        ### PANTALLA ###
        self.screen = pygame.display.set_mode((c.ANCHO, c.ALTO))
        pygame.display.set_caption("Green Study")
        
        self.icon_image = pygame.image.load("assets//images//regadera.png")
        pygame.display.set_icon(self.icon_image)

        self.background = pygame.image.load("assets//images//Background.png")
        self.blurred_background = pygame.transform.gaussian_blur(self.background, 10)

        # Controlar el frame rate
        self.clock = pygame.time.Clock()

        ### ESCALAR IMAGENES ###

        def escale_img(image, scale):
            w = image.get_width()
            h = image.get_height()
            new_image = pygame.transform.scale(image, (w * scale, h * scale))
            return new_image

        self.font = pygame.font.SysFont("Arial", 24)
        self.escale_img = escale_img
        self.screen.fill((0,0,0))
        self.Play_text = self.font.render(f"Menu Screen", True, (255, 255, 255))
        self.screen.blit(self.Play_text, (320, 200))

        # Boton para iniciar el juego
        self.play_image = pygame.image.load("assets//images//start.jpg")
        self.play_image = escale_img(self.play_image, c.SCALE_FOR_SKIP)
        self.play_icon = Time_skip(self.play_image, 380, 300) 
        self.play_icon.draw(self.screen)

        self.game = 1

        menu_music()


    def run(self):
        while(True):
            self.screen.blit(self.blurred_background)
            self.play_icon.draw(self.screen)
            self.screen.blit(self.Play_text, (320, 200))
            for event in pygame.event.get():
                self.position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_icon.image_shape.collidepoint(self.position):
                        stop_music()
                        while self.game == 1:
                            self.game_loop = Game_Loop(self.screen, self.font, self.escale_img,self.clock)
                            self.game_loop_run = self.game_loop.run()
                            self.game_over = Game_Over(self.screen, self.font, self.escale_img,self.clock, self.blurred_background, self.game_loop_run[0], self.game_loop_run[1], self.game_loop_run[2])
                            self.game_over_run = self.game_over.run()
                            self.game == self.game_over_run
                        stop_music()
                        menu_music()
                            
                            
            
            self.clock.tick(c.FPS)
            pygame.display.update()

menu = Menu()
menu.run()