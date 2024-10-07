import pygame
import CONSTANTES as c
from objects.botones import Time_skip
import sys
from game_loop import Game_Loop
from objects.object import Object

class Game_Over:
    def __init__(self, screen, font, escale_img, clock, background, type, plant_achieved, score):
        self.clock = clock
        self.screen = screen
        self.font = font
        self.type = type
        self.background = background
        self.escale_img = escale_img
        # self.plant_achieved = plant_achieved
        self.plant_achieved = plant_achieved
        self.plant_achieved_rect = self.plant_achieved.get_rect(center=(425, 260))
        self.score = score
        self.pixel_font = pygame.font.Font("assets//fonts//PressStart2P-Regular.ttf", 18)

        # Boton para volver a jugar
        self.scroll = Object("assets//images//Game-over-screen-fondo.png", c.CENTER[0],c.CENTER[1])
        self.win = Object("assets//images//Game-over-screen-ganaste.png", c.CENTER[0], 230)
        self.lose = Object("assets//images//Game-over-screen-perdiste.png", c.CENTER[0], 230)
        self.A = Object("assets//images//Game-over-screen-A.png", 300, 225)
        self.B = Object("assets//images//Game-over-screen-B.png", 300, 225)
        self.C = Object("assets//images//Game-over-screen-C.png", 300, 225)
        self.D = Object("assets//images//Game-over-screen-D.png", 300, 225)
        self.F = Object("assets//images//Game-over-screen-F.png", 300, 225)

        self.menu = Object("assets//images//Game-over-screen-menu.png", 245, 170)
        self.again = Object("assets//images//Game-over-screen-retry.png", 355, 235)
        
        self.score_text = self.pixel_font.render(f"Score: {self.score}", True, 'brown')
        self.score_text_rect = self.score_text.get_rect(center=(c.CENTER[0], 440))

        self.loop = True
    def run(self):
        while self.loop:
            # Lleno la pantalla en negro y pongo 'Game Over'
            self.scroll.draw(self.screen)

            if self.type == 1:
                self.win.draw(self.screen)
                if self.score == 360:
                    self.A.draw(self.screen)
                if self.score == 280:
                    self.B.draw(self.screen)
                if self.score == 230:
                    self.C.draw(self.screen)
                if self.score == 180:
                    self.D.draw(self.screen)
            else:
                self.lose.draw(self.screen)
                self.F.draw(self.screen)

            self.screen.blit(self.score_text, self.score_text_rect)
            self.menu.draw(self.screen)
            self.again.draw(self.screen)
            self.screen.blit(self.plant_achieved,self.plant_achieved_rect)
                
            
            for event in pygame.event.get():
                self.mouse_position = pygame.mouse.get_pos()
                self.mouse_mask = pygame.mask.Mask((1, 1), fill=True)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Vuelvo a jugar si apreto el boton
                    if self.menu.check_collision(self.position, self.mouse_mask) == 1:
                        return 0
                    if self.again.check_collision(self.position, self.mouse_mask) == 1:
                        return 1


            self.clock.tick(c.FPS)
            pygame.display.update()
        self.game_loop = Game_Loop(self.screen, self.font, self.escale_img, self.clock)
        self.game_loop.run()
