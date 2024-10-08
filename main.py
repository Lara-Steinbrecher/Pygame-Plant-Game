import pygame
import CONSTANTES as c
from objects.botones import Time_skip
from game_loop import Game_Loop
from game_over import Game_Over
from tutorial import Tutorial
import sys
from menu_music import menu_music, stop_music
from objects.object import Object

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

        self.main_screen = pygame.image.load("assets//images//main_screen.png")

        self.start_button = Object("assets//images//start.png", 420,400)
        self.exit_button = Object("assets//images//exit.png", 420,450)
        self.game = 1

        menu_music()


    def run(self):
        while(True):
            self.screen.blit(self.blurred_background)
            self.screen.blit(self.main_screen)
            self.start_button.draw(self.screen)
            self.exit_button.draw(self.screen)


            for event in pygame.event.get():
                self.mouse_position = pygame.mouse.get_pos()
                self.mouse_mask = pygame.mask.Mask((1, 1), fill=True)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.check_collision(self.mouse_position, self.mouse_mask) == 1:
                        stop_music()
                        while self.game == 1:
                            self.tutorial = Tutorial(self.screen, self.blurred_background, self.clock)
                            self.tutorial.run()
                            self.game_loop = Game_Loop(self.screen, self.font, self.escale_img,self.clock)
                            self.game_loop_run = self.game_loop.run()
                            self.game_over = Game_Over(self.screen, self.font, self.escale_img,self.clock, self.blurred_background, self.game_loop_run[0], self.game_loop_run[1], self.game_loop_run[2])
                            self.game_over_run = self.game_over.run()
                            self.game == self.game_over_run
                        stop_music()
                        menu_music()
                    if self.exit_button.check_collision(self.mouse_position, self.mouse_mask) == 1:
                        pygame.quit()
                        sys.exit()
                            
                            
            
            self.clock.tick(c.FPS)
            pygame.display.update()

menu = Menu()
menu.run()