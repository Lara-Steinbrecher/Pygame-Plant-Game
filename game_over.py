import pygame
import CONSTANTES as c
from personaje import Planta
from botones import Icon, Boton, Mood, Time_skip
from obstacles import Obstacle
import random
import sys
from play import game_loop


screen = pygame.display.set_mode((c.ANCHO, c.ALTO))
pygame.display.set_caption("DEMOPLANTA")
background = pygame.image.load("assets//images//Background.jpg")



clock = pygame.time.Clock()

### ESCALAR IMAGENES ###

def escale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (w * scale, h * scale))
    return new_image

# Pantalla de game over, pasa cuando algunos de los valores llega a 0
def game_over ():

    # Font para los textos (provisional)
    font = pygame.font.SysFont("Arial", 24)

    while True:
        # Lleno la pantalla en negro y pongo 'Game Over'
        screen.fill((0,0,0))
        Game_Over_text = font.render(f"Game Over", True, (255, 255, 255))
        screen.blit(Game_Over_text, (320, 200))

        # Boton para volver a jugar
        try_again_image = pygame.image.load("assets//images//start.jpg")
        try_again_image = escale_img(try_again_image, c.SCALE_FOR_SKIP)
        try_again_icon = Time_skip(try_again_image, 380, 300)  
        try_again_icon.draw(screen)  

        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Vuelvo a jugar si apreto el boton
                if try_again_icon.image_shape.collidepoint(position):
                    game_loop()

        clock.tick(c.FPS)
        pygame.display.update()