import pygame
import CONSTANTES as c
from personaje import Planta
from botones import Icon, Boton, Mood, Time_skip
from obstacles import Obstacle
import random
import sys
from game_over import game_over
from play import game_loop

pygame.init() 

### PANTALLA ###

screen = pygame.display.set_mode((c.ANCHO, c.ALTO))
pygame.display.set_caption("DEMOPLANTA")
background = pygame.image.load("assets//images//Background.jpg")

# Controlar el frame rate 
clock = pygame.time.Clock()

### ESCALAR IMAGENES ###

def escale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image, (w * scale, h * scale))
    return new_image

# Font para los textos (provisional)
font = pygame.font.SysFont("Arial", 24)

##################################################################

# Loop del menu
while True:
    # Pantalla negra y texto
    screen.fill((0,0,0))
    Play_text = font.render(f"Menu Screen", True, (255, 255, 255))
    screen.blit(Play_text, (320, 200))

    # Boton para iniciar el juego
    play_image = pygame.image.load("assets//images//start.jpg")
    play_image = escale_img(play_image, c.SCALE_FOR_SKIP)
    play_icon = Time_skip(play_image, 380, 300)  
    play_icon.draw(screen)  

    for event in pygame.event.get():
        position = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_icon.image_shape.collidepoint(position):
                game_loop()
                game_over()

    clock.tick(c.FPS)
    pygame.display.update()