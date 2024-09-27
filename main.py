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


# Font para los textos (provisional)
font = pygame.font.SysFont("Arial", 24)

# Loop principal (hay uno para cada opcion del menu)
def game_loop():
    
    ### PLANTA ###
    # Cargo imagen de planta
    planta_image = pygame.image.load("assets//images//plant//plantaprueba.jpg")
    planta_image = escale_img(planta_image, c.SCALE_FOR_PLANT)
    planta = Planta(planta_image)

    ### TIME ###
    # Cargo imagen de reloj
    time_image = pygame.image.load("assets//images//time.jpg")
    time_image = escale_img(time_image, c.SCALE_FOR_TIME)
    time_icon = Icon(time_image, 625, 200)

    ### TIME SKIP ###
    # Cargo boton para el double time
    skip_image = pygame.image.load("assets//images//start.jpg")
    skip_image = escale_img(skip_image, c.SCALE_FOR_SKIP)
    skip_icon = Time_skip(skip_image, 570, 200)

    ### POST IT ###
    # Que hace esto???
    flecha_arriba_image = pygame.image.load("assets//images//flecha_arriba.jpg")
    flecha_abajo_image = pygame.image.load("assets//images//flecha_abajo.jpg")
    flecha_media_image = pygame.image.load("assets//images//flecha_media.jpg")
    flecha_arriba_image = escale_img(flecha_arriba_image, c.SCALE_FOR_POSTIT)
    flecha_abajo_image = escale_img(flecha_abajo_image, c.SCALE_FOR_POSTIT)
    flecha_media_image = escale_img(flecha_media_image, c.SCALE_FOR_POSTIT)

    postit = Mood(flecha_abajo_image, flecha_media_image, flecha_arriba_image, 295,370)

    ### HUGE TIME ###
    # Same, que queres cargar???
    huge_time_image = pygame.image.load("assets//images//time.jpg")
    huge_time_image = escale_img(huge_time_image, c.SCALE_FOR_HUGE_TIME)
    huge_time_icon = Icon(huge_time_image, 0, 0)

    ### Variables clickeables ###

    ### AGUA ###
    # Cargo imagen del agua y su boton (el on es invisible)
    agua_image = pygame.image.load("assets//images//water.jpg")
    agua_image = escale_img(agua_image, c.SCALE_FOR_WATER)
    agua_icon = Icon(agua_image, 625,110)

    boff_agua_image = pygame.image.load("assets//images//off.jpg")
    bon_agua_image = pygame.image.load("assets//images//on.jpg")
    boff_agua_image = escale_img(boff_agua_image, c.SCALE_FOR_BOTTOM_WATER)
    bon_agua_image = escale_img(bon_agua_image, c.SCALE_FOR_BOTTOM_WATER)

    boton_agua_icon = Boton(bon_agua_image, boff_agua_image, 570,110)

    ### LUZ ###
    # Cargo el boton de luz (el on es invisivle)
    luz_image = pygame.image.load("assets//images//luz.jpg")
    luz_image = escale_img(luz_image, c.SCALE_FOR_WATER)
    luz_icon = Icon(luz_image, 470,110)

    boff_luz_image = pygame.image.load("assets//images//off.jpg")
    bon_luz_image = pygame.image.load("assets//images//on.jpg")
    boff_luz_image = escale_img(boff_luz_image, c.SCALE_FOR_BOTTOM_WATER)
    bon_luz_image = escale_img(bon_luz_image, c.SCALE_FOR_BOTTOM_WATER)

    boton_luz_icon = Boton(bon_luz_image, boff_luz_image, 420,110)

    # Timer
    MY_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(MY_EVENT, 1000) # cada 1 segundo
    reloj = 0
    # Cambia cuando estoy manteniendo el boton de acelerar tiempo
    double_time = False

    # Variables para saber que boton tengo que mostrar
    var_agua = 1
    var_luz = 1

    # Variables que se activan cuando se activa un minigame
    water_minigame_on = False
    light_minigame_on = False

    run = True
    while run: 
        # Dibujo el fondo y todas las imagenes
        screen.blit(background,(0,0)) #fondo centrado
        planta.draw(screen)
        boton_agua_icon.draw(var_agua, screen)
        boton_luz_icon.draw(var_luz, screen)
        agua_icon.draw(screen)
        luz_icon.draw(screen)
        postit.draw(screen, 75)
        time_icon.draw(screen)
        skip_icon.draw(screen)   

        # Escribo valores que necesito trackear para jugar, como necesidades de la planta o tiempo
        timer_text = font.render(f"Timer: {reloj}", True, (255, 255, 255))
        agua_text = font.render(f"Agua: {boton_agua_icon.need}", True, (255, 255, 255))
        luz_text = font.render(f"Luz: {boton_luz_icon.need}", True, (255, 255, 255))
        screen.blit(timer_text, (10, 10))
        screen.blit(agua_text, (10, 50))
        screen.blit(luz_text, (10, 90))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            # Timer, te da doble puntaje mientras lo mantengas presionado al boton
            if event.type == MY_EVENT:
                if double_time == True:
                    reloj = reloj + 2
                    boton_agua_icon.need = boton_agua_icon.need - random.randint (5, 10)
                    boton_luz_icon.need = boton_luz_icon.need - random.randint (5, 10)
                else:
                    reloj = reloj + 1
                    boton_agua_icon.need = boton_agua_icon.need - random.randint (0, 5)
                    boton_luz_icon.need = boton_luz_icon.need - random.randint (0, 5)

            # Si clickeo, me fijo cual boton es:
            #   Para el boton de skip, duplico el puntaje y para los demás le cambio entre estado on y off
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

            # Dejo de tener doble puntaje si dejo de apretar el boton
            if event.type == pygame.MOUSEBUTTONUP:
                double_time = False
        
        # Termina el loop si algunos de los valores de necesidad de la planta bajan a 0 (pierdo)
        if boton_agua_icon.need <= 0 or boton_luz_icon.need <= 0:
            run = False
        
        if water_minigame_on == True:
            water_minigame()

        pygame.display.update()
        clock.tick(c.FPS)


def water_minigame():
    jump = False
    # Digamos
    ground = MINIGAME_X - PERSON_ALTO - 10
    person_X = PERSON_X
    person_Y = ground
    person_Y_speed = 0

    ### Draw the background ###

    background_image_unescaled = pygame.image.load("assets//images//waterMiniGameBackground.jpg")
    background_image = escale_img(background_image_unescaled, c.SCALE_FOR_PLANT)
    background_rect = background_image.get_rect()
    screen.blit(background_image, background_rect)
    background_rect = background_image.get_rect()
    background_rect.center = (ANCHO // 2, ALTO // 2) # Estoy usando doble barra para que quede entero (cosa de pixeles), fijate de lo mismo

    ### Draw the person ###
    person_image_unescaled = pygame.image.load("assets//images//waterMiniGameBackground.jpg")
    person_image = escale_img(person_image_unescaled, c.SCALE_FOR_PLANT)
    person_rect = person_image.get_rect()
    screen.blit(person_image, person_rect)
    person_rect = person_image.get_rect()
    person_rect.center = (person_X, person_Y)
    
    ### Draw the obstacles ###
    obstacle_image_unescaled = pygame.image.load("assets//images//waterMiniGameBackground.jpg")
    obstacle_image = escale_img(obstacle_image_unescaled, c.SCALE_FOR_PLANT)
    random.randrange(12, 36)
    obstacle1 = Obstacle(obstacle_image, random.randrange(100, 200),ground)
    obstacle1.draw()
    obstacle2 = Obstacle(obstacle_image, random.randrange(250, 350),ground)
    obstacle2.draw()
    obstacle3 = Obstacle(obstacle_image, random.randrange(400, 500), ground)
    obstacle3.draw()
    

    ### Draw the tap ###
    tap_image_unescaled = pygame.image.load("assets//images//waterMiniGameBackground.jpg")
    tap_image = escale_img(tap_image_unescaled, c.SCALE_FOR_PLANT)
    tap_rect = tap_image.get_rect()
    screen.blit(tap_image, tap_rect)
    tap_rect = tap_image.get_rect()
    tap_rect.center = (TAP_X, ground)


    for event in pygame.event.get():
        if event.type == pygame.K_D:
            PERSON_X -= PERSON_SPEED
        if event.type == pygame.K_W:
            PERSON_Y += PERSON_SPEED
        if event.type == pygame.K_SPACE:
            if (jump == False):
                # Si no estoy saltando, empiezo a contar que estoy saltando y me agrego velocidad 
                # (lo que voy a agregar a mi posición)
                jump = True
                person_vertical_speed = -jump
            else:
                # Si ya estoy saltando, cambio mi posición a más alto y me bajo la velocidad, esto hasta que baje hasta
                # el suelo
                person_Y += person_Y_speed
                person_Y_speed += PERSON_GRAVITY

    if PERSON_Y == ground: # Si estoy a nivel del suelo, mi velocidad de caida es 0 y dejo de saltar
        jump = False
        person_Y_speed = 0

    # Colisión con bordes
    #   Lado izquierdo
    if person_X < 0:
        person_X = 0
    #   Lado derecho
    if person_X > ANCHO - PERSON_ANCHO:
        person_X = ANCHO - PERSON_ANCHO

    # Colisión de personaje con obstaculo
    if person_rect.colliderect(obstacle_rect1.shape) or person_rect.colliderect(obstacle_rect2.shape) or person_rect.colliderect(obstacle_rect3.shape):
        person_X = PERSON_X
    if person_rect.colliderect(tap_rect):
        water_minigame_on = False
    

# Pantalla de game over, pasa cuando algunos de los valores llega a 0
def game_over ():
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Vuelvo a jugar si apreto el boton
                if try_again_icon.image_shape.collidepoint(position):
                    game_loop()

        clock.tick(c.FPS)
        pygame.display.update()

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