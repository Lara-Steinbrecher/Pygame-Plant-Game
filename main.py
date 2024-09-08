import pygame
import CONSTANTES as c
from personaje import Planta
from botones import Icon, Boton, Mood, Time_skip
import random

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

huge_time_icon = Icon(huge_time_image, 370, 220)

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

### VARIABLES VARIABLES ###

agua = ""
luz = ""
temperatura = ""
nutrientes = ""

activador = ""

agua_rate = 20

var_agua = 1
var_luz = 1

reloj = 0
MY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MY_EVENT, 1000) # cada 1 segundo

run = True
while run:

    # Defino FPS
    clock.tick(c.FPS)
    screen.blit(background,(0,0)) #fondo centrado
    planta.draw(screen)
    boton_agua_icon.draw(var_agua, screen)
    boton_luz_icon.draw(var_luz, screen)
    agua_icon.draw(screen)
    luz_icon.draw(screen)
    postit.draw(screen, 75)
    time_icon.draw(screen)
    skip_icon.draw(screen)   

    activador = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
        if event.type == MY_EVENT:
            reloj = reloj + 1
            print(reloj)

        if pygame.mouse.get_pressed()[0]:
            clicked = True
            position = pygame.mouse.get_pos()

            if boton_agua_icon.off_shape.collidepoint(position) or boton_agua_icon.on_shape.collidepoint(position):
                var_agua = -var_agua
                if var_agua < 0:
                    agua = True
                elif var_agua > 0:
                    agua = False
            print(clicked, position)
            if boton_luz_icon.off_shape.collidepoint(position) or boton_luz_icon.on_shape.collidepoint(position):
                var_luz = -var_luz
                if var_luz < 0:
                    luz = True
                elif var_luz > 0:
                    luz = False
            
            if skip_icon.image_shape.collidepoint(position):
                
                activador = True
                reloj = reloj +1
                print(reloj)

            print(clicked, position, agua_rate)
        if not pygame.mouse.get_pressed()[0] and clicked:
            clicked = False
            activador = False
            print(clicked, activador)

    pygame.display.update()

pygame.quit()