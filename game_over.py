import pygame
import CONSTANTES as c
from objects.botones import Time_skip
import sys
from game_loop import Game_Loop

class Game_Over:
    def __init__(self, screen, font, escale_img, clock):
        self.clock = clock
        self.screen = screen
        self.font = font
        self.escale_img = escale_img

        # Boton para volver a jugar
        self.try_again_image = pygame.image.load("assets//images//start.jpg")
        self.try_again_image = escale_img(self.try_again_image, c.SCALE_FOR_SKIP)
        self.try_again_icon = Time_skip(self.try_again_image, 380, 300)

        # Boton para ir al menu
        self.menu_image = pygame.image.load("assets//images//start.jpg")
        self.menu_image = escale_img(self.menu_image, c.SCALE_FOR_SKIP)
        self.menu_icon = Time_skip(self.menu_image, 380, 300)

        self.loop = True
    def run(self):
        self.loop = True
        while self.loop:
            # Lleno la pantalla en negro y pongo 'Game Over'
            self.screen.fill((0,0,0))
            self.Game_Over_text = self.font.render(f"Game Over", True, (255, 255, 255))
            self.screen.blit(self.Game_Over_text, (320, 200))
            self.try_again_icon.draw(self.screen) 
            for event in pygame.event.get():
                position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Vuelvo a jugar si apreto el boton
                    if self.try_again_icon.image_shape.collidepoint(position):
                        self.loop = False

            self.clock.tick(c.FPS)
            pygame.display.update()
        self.game_loop = Game_Loop(self.screen, self.font, self.escale_img, self.clock)
        self.game_loop.run()
