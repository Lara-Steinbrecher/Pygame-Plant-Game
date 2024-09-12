import pygame
import CONSTANTES as c
from personaje import Planta
from botones import Icon, Boton, Mood, Time_skip
import random
import sys

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

font = pygame.font.SysFont("Arial", 24)

def game_loop():
    ### PLANTA ###

    planta_image = pygame.image.load("assets//images//plant//plantaprueba.jpg")
    planta_image = escale_img(planta_image, c.SCALE_FOR_PLANT)
    planta = Planta(planta_image)

    clicked = ""

    ### TIME ###

    time_image = pygame.image.load("assets//images//time.jpg")
    time_image = escale_img(time_image, c.SCALE_FOR_TIME)

    time_icon = Icon(time_image, 625, 200)

    ### HUGE TIME ###

    huge_time_image = pygame.image.load("assets//images//time.jpg")
    huge_time_image = escale_img(huge_time_image, c.SCALE_FOR_HUGE_TIME)

    huge_time_icon = Icon(huge_time_image, 0, 0)

    ### TIME SKIP ###

    skip_image = pygame.image.load("assets//images//start.jpg")
    skip_image = escale_img(skip_image, c.SCALE_FOR_SKIP)

    skip_icon = Time_skip(skip_image, 570, 200)

    ### POST IT ###

    flecha_arriba_image = pygame.image.load("assets//images//flecha_arriba.jpg")
    flecha_abajo_image = pygame.image.load("assets//images//flecha_abajo.jpg")
    flecha_media_image = pygame.image.load("assets//images//flecha_media.jpg")
    flecha_arriba_image = escale_img(flecha_arriba_image, c.SCALE_FOR_POSTIT)
    flecha_abajo_image = escale_img(flecha_abajo_image, c.SCALE_FOR_POSTIT)
    flecha_media_image = escale_img(flecha_media_image, c.SCALE_FOR_POSTIT)

    postit = Mood(flecha_abajo_image, flecha_media_image, flecha_arriba_image, 295,370)

    ### Variables clickeables ###

    ### AGUA ###

    agua_image = pygame.image.load("assets//images//water.jpg")
    agua_image = escale_img(agua_image, c.SCALE_FOR_WATER)
    agua_icon = Icon(agua_image, 625,110)

    boff_agua_image = pygame.image.load("assets//images//off.jpg")
    bon_agua_image = pygame.image.load("assets//images//on.jpg")
    boff_agua_image = escale_img(boff_agua_image, c.SCALE_FOR_BOTTOM_WATER)
    bon_agua_image = escale_img(bon_agua_image, c.SCALE_FOR_BOTTOM_WATER)

    boton_agua_icon = Boton(bon_agua_image, boff_agua_image, 570,110)

    ### LUZ ###

    luz_image = pygame.image.load("assets//images//luz.jpg")
    luz_image = escale_img(luz_image, c.SCALE_FOR_WATER)
    luz_icon = Icon(luz_image, 470,110)

    boff_luz_image = pygame.image.load("assets//images//off.jpg")
    bon_luz_image = pygame.image.load("assets//images//on.jpg")
    boff_luz_image = escale_img(boff_luz_image, c.SCALE_FOR_BOTTOM_WATER)
    bon_luz_image = escale_img(bon_luz_image, c.SCALE_FOR_BOTTOM_WATER)

    boton_luz_icon = Boton(bon_luz_image, boff_luz_image, 420,110)

    MY_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(MY_EVENT, 1000) # cada 1 segundo

    ### VARIABLES VARIABLES ###
    var_agua = 1
    var_luz = 1
    double_time = False
    reloj = 0
    
    run = True
    while run: 
        screen.blit(background,(0,0)) #fondo centrado
        planta.draw(screen)
        boton_agua_icon.draw(var_agua, screen)
        boton_luz_icon.draw(var_luz, screen)
        agua_icon.draw(screen)
        luz_icon.draw(screen)
        postit.draw(screen, 75)
        time_icon.draw(screen)
        skip_icon.draw(screen)   

        timer_text = font.render(f"Timer: {reloj}", True, (255, 255, 255))
        agua_text = font.render(f"Agua: {boton_agua_icon.need}", True, (255, 255, 255))
        luz_text = font.render(f"Luz: {boton_luz_icon.need}", True, (255, 255, 255))
        screen.blit(timer_text, (10, 10))
        screen.blit(agua_text, (10, 50))
        screen.blit(luz_text, (10, 90))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == MY_EVENT:
                if double_time == True:
                    reloj = reloj + 2
                    boton_agua_icon.need = boton_agua_icon.need - random.randint (5, 10)
                    boton_luz_icon.need = boton_luz_icon.need - random.randint (5, 10)
                else:
                    reloj = reloj + 1
                    boton_agua_icon.need = boton_agua_icon.need - random.randint (0, 5)
                    boton_luz_icon.need = boton_luz_icon.need - random.randint (0, 5)

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if event.button == 1:
                    if skip_icon.image_shape.collidepoint(position):
                        double_time = True
                    if boton_agua_icon.off_shape.collidepoint(position) or boton_agua_icon.on_shape.collidepoint(position):
                        var_agua = -var_agua
                        if var_agua < 0:
                            agua = True
                            boton_agua_icon.need = 100
                        elif var_agua > 0:
                            agua = False
                    if boton_luz_icon.off_shape.collidepoint(position) or boton_luz_icon.on_shape.collidepoint(position):
                        var_luz = -var_luz
                        if var_luz < 0:
                            luz = True
                            boton_luz_icon.need = 100
                        elif var_luz > 0:
                            luz = False

            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                double_time = False
        
        if boton_agua_icon.need <= 0 or boton_luz_icon.need <= 0:
            run = False
        
        pygame.display.update()
        clock.tick(c.FPS)

def game_over ():
    while True:
        screen.fill((0,0,0))
        Game_Over_text = font.render(f"Game Over", True, (255, 255, 255))
        screen.blit(Game_Over_text, (320, 200))

        try_again_image = pygame.image.load("assets//images//start.jpg")
        try_again_image = escale_img(try_again_image, c.SCALE_FOR_SKIP)
        try_again_icon = Time_skip(try_again_image, 380, 300)  
        try_again_icon.draw(screen)  

        for event in pygame.event.get():
            position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if try_again_icon.image_shape.collidepoint(position):
                    game_loop()

        clock.tick(c.FPS)
        pygame.display.update()


while True:
    screen.fill((0,0,0))
    Play_text = font.render(f"Menu Screen", True, (255, 255, 255))
    screen.blit(Play_text, (320, 200))

    play_image = pygame.image.load("assets//images//start.jpg")
    play_image = escale_img(play_image, c.SCALE_FOR_SKIP)
    play_icon = Time_skip(play_image, 380, 300)  
    play_icon.draw(screen)  

    for event in pygame.event.get():
        position = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_icon.image_shape.collidepoint(position):
                game_loop()
                game_over()

    clock.tick(c.FPS)
    pygame.display.update()



# pygame.quit()
# sys.exit()

# Es mejor ponerlo como clase para hacer la parte de menu inicial