import pygame
import CONSTANTES as c
from objects.planta import Planta
from objects.botones import Icon, Boton, Mood, Time_skip
import random
import sys
from minijuegos.light_minigame import Light_Minigame
from minijuegos.water_minigame import Water_Minigame
from minijuegos.soil_minigame import Soil_Minigame
from minijuegos.temp_minigame import Temp_Minigame


class Game_Loop():
    def __init__(self, screen, font, escale_img, clock):
        self.clock = clock
        self.screen = screen
        self.font = font
        self.escale_img = escale_img

        self.background = pygame.image.load("assets//images//Background.png")

        ### PLANTA ###
        # Cargo imagen de planta
        self.planta_image = pygame.image.load("assets//images//plant//plantaprueba.jpg")
        self.planta_image = escale_img(self.planta_image, c.SCALE_FOR_PLANT)
        self.planta = Planta(self.planta_image)

        ### TIME ###
        # Cargo imagen de reloj
        self.time_image = pygame.image.load("assets//images//time.jpg")
        self.time_image = escale_img(self.time_image, c.SCALE_FOR_TIME)
        self.time_icon = Icon(self.time_image, 625, 200)

        ### TIME SKIP ###
        # Cargo boton para el double time
        self.skip_image = pygame.image.load("assets//images//start.jpg")
        self.skip_image = escale_img(self.skip_image, c.SCALE_FOR_SKIP)
        self.skip_icon = Time_skip(self.skip_image, 570, 200)

        ### POST IT ###
        # Que hace esto???
        self.flecha_arriba_image = pygame.image.load("assets//images//flecha_arriba.jpg")
        self.flecha_abajo_image = pygame.image.load("assets//images//flecha_abajo.jpg")
        self.flecha_media_image = pygame.image.load("assets//images//flecha_media.jpg")
        self.flecha_arriba_image = escale_img(self.flecha_arriba_image, c.SCALE_FOR_POSTIT)
        self.flecha_abajo_image = escale_img(self.flecha_abajo_image, c.SCALE_FOR_POSTIT)
        self.flecha_media_image = escale_img(self.flecha_media_image, c.SCALE_FOR_POSTIT)

        self.postit = Mood(self.flecha_abajo_image, self.flecha_media_image, self.flecha_arriba_image, 295,370)

        ### HUGE TIME ###
        # Same, que queres cargar???
        self.huge_time_image = pygame.image.load("assets//images//time.jpg")
        self.huge_time_image = escale_img(self.huge_time_image, c.SCALE_FOR_HUGE_TIME)
        self.huge_time_icon = Icon(self.huge_time_image, 0, 0)

        ### Variables clickeables ###

        ### AGUA ###
        # Cargo imagen del agua y su boton (el on es invisible)
        self.agua_image = pygame.image.load("assets//images//water.jpg")
        self.agua_image = escale_img(self.agua_image, c.SCALE_FOR_WATER)
        self.agua_icon = Icon(self.agua_image, 625,110)

        self.boff_agua_image = pygame.image.load("assets//images//off.jpg")
        self.bon_agua_image = pygame.image.load("assets//images//on.jpg")
        self.boff_agua_image = escale_img(self.boff_agua_image, c.SCALE_FOR_BOTTOM_WATER)
        self.bon_agua_image = escale_img(self.bon_agua_image, c.SCALE_FOR_BOTTOM_WATER)

        self.boton_agua_icon = Boton(self.bon_agua_image, self.boff_agua_image, 570,110)

        ### LUZ ###
        # Cargo el boton de luz (el on es invisivle)
        self.luz_image = pygame.image.load("assets//images//luz.jpg")
        self.luz_image = escale_img(self.luz_image, c.SCALE_FOR_WATER)
        self.luz_icon = Icon(self.luz_image, 470,110)

        self.boff_luz_image = pygame.image.load("assets//images//off.jpg")
        self.bon_luz_image = pygame.image.load("assets//images//on.jpg")
        self.boff_luz_image = escale_img(self.boff_luz_image, c.SCALE_FOR_BOTTOM_WATER)
        self.bon_luz_image = escale_img(self.bon_luz_image, c.SCALE_FOR_BOTTOM_WATER)

        self.boton_luz_icon = Boton(self.bon_luz_image, self.boff_luz_image, 420,110)

        ### SOIL ###
        self.soil_image = pygame.image.load("assets//images//luz.jpg")
        self.soil_image = escale_img(self.soil_image, c.SCALE_FOR_WATER)
        self.soil_icon = Icon(self.soil_image, 470,210)

        self.boff_soil_image = pygame.image.load("assets//images//off.jpg")
        self.bon_soil_image = pygame.image.load("assets//images//on.jpg")
        self.boff_soil_image = escale_img(self.boff_luz_image, c.SCALE_FOR_BOTTOM_WATER)
        self.bon_soil_image = escale_img(self.bon_luz_image, c.SCALE_FOR_BOTTOM_WATER)

        self.boton_soil_icon = Boton(self.bon_soil_image, self.boff_soil_image, 420,210)

        ### TEMPERATURA ###
        self.temp_image = pygame.image.load("assets//images//luz.jpg")
        self.temp_image = escale_img(self.temp_image, c.SCALE_FOR_WATER)
        self.temp_icon = Icon(self.temp_image, 470,310)

        self.boff_temp_image = pygame.image.load("assets//images//off.jpg")
        self.bon_temp_image = pygame.image.load("assets//images//on.jpg")
        self.boff_temp_image = escale_img(self.boff_temp_image, c.SCALE_FOR_BOTTOM_WATER)
        self.bon_temp_image = escale_img(self.bon_temp_image, c.SCALE_FOR_BOTTOM_WATER)

        self.boton_temp_icon = Boton(self.bon_temp_image, self.boff_temp_image, 420,310)

        # Timer
        self.MY_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.MY_EVENT, 1000) # cada 1 segundo
        self.reloj = 0
        # Cambia cuando estoy manteniendo el boton de acelerar tiempo
        self.double_time = False

        # Variables para saber que boton tengo que mostrar
        self.var_agua = 1
        self.var_luz = 1
        self.var_soil = 1
        self.var_temp = 1

        # Variables que se activan cuando se activa un minigame
        self.water_minigame_on = False
        self.light_minigame_on = False
        self.soil_minigame_on = False
        self.temp_minigame_on = False

        self.spacebar_pressed = False
        self.mouse_pressed = False
        self.pressed_letter = 0
    
    def run (self):
        self.loop = True
        while self.loop: 
            # Dibujo el fondo y todas las imagenes
            self.screen.blit(self.background,(0,0)) #fondo centrado
            #self.planta.draw(self.screen)
            self.boton_agua_icon.draw(self.var_agua, self.screen)
            self.boton_luz_icon.draw(self.var_luz, self.screen)
            self.boton_soil_icon.draw(self.var_soil, self.screen)
            self.boton_temp_icon.draw(self.var_temp, self.screen)
            self.agua_icon.draw(self.screen)
            self.luz_icon.draw(self.screen)
            self.soil_icon.draw(self.screen)
            self.temp_icon.draw(self.screen)
            self.postit.draw(self.screen, 75)
            self.time_icon.draw(self.screen)
            self.skip_icon.draw(self.screen)   

            # Escribo valores que necesito trackear para jugar, como necesidades de la planta o tiempo
            self.timer_text = self.font.render(f"Timer: {self.reloj}", True, (255, 255, 255))
            self.agua_text = self.font.render(f"Agua: {self.boton_agua_icon.need}", True, (255, 255, 255))
            self.luz_text = self.font.render(f"Luz: {self.boton_luz_icon.need}", True, (255, 255, 255))
            self.soil_text = self.font.render(f"Soil: {self.boton_soil_icon.need}", True, (255, 255, 255))
            self.temp_text = self.font.render(f"Temp: {self.boton_temp_icon.need}", True, (255, 255, 255))
            self.screen.blit(self.timer_text, (10, 10))
            self.screen.blit(self.agua_text, (10, 50))
            self.screen.blit(self.luz_text, (10, 90))
            self.screen.blit(self.soil_text, (10, 130))
            self.screen.blit(self.temp_text, (10, 170))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Timer, te da doble puntaje mientras lo mantengas presionado al boton
                if event.type == self.MY_EVENT:
                    if self.double_time == True:
                        self.reloj = self.reloj + 2
                        self.boton_agua_icon.need = self.boton_agua_icon.need - random.randint (5, 10)
                        self.boton_luz_icon.need = self.boton_luz_icon.need - random.randint (5, 10)
                        self.boton_soil_icon.need = self.boton_soil_icon.need - random.randint (5, 10)
                        self.boton_temp_icon.need = self.boton_temp_icon.need - random.randint (5, 10)
                    else:
                        self.reloj = self.reloj + 1
                        self.boton_agua_icon.need = self.boton_agua_icon.need - random.randint (0, 5)
                        self.boton_luz_icon.need = self.boton_luz_icon.need - random.randint (0, 5)
                        self.boton_soil_icon.need = self.boton_soil_icon.need - random.randint (0, 5)
                        self.boton_temp_icon.need = self.boton_temp_icon.need - random.randint (0, 5)

                # Si clickeo, me fijo cual boton es:
                #   Para el boton de skip, duplico el puntaje y para los demás le cambio entre estado on y off
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.position = pygame.mouse.get_pos()
                    self.mouse_pressed = True
                    if self.water_minigame_on == False and self.light_minigame_on == False and self.soil_minigame_on == False and self.temp_minigame_on == False:
                        if event.button == 1:
                            if self.skip_icon.image_shape.collidepoint(self.position):
                                self.double_time = True
                            if self.boton_agua_icon.off_shape.collidepoint(self.position) or self.boton_agua_icon.on_shape.collidepoint(self.position):
                                self.water_minigame_on = True
                                self.water_minigame = Water_Minigame(self.screen, self.font, self.escale_img)
                                self.var_agua = -self.var_agua
                                if self.var_agua < 0:
                                    self.agua = True
                                    self.boton_agua_icon.need = 100
                                elif self.var_agua > 0:
                                    self.agua = False
                            if self.boton_luz_icon.off_shape.collidepoint(self.position) or self.boton_luz_icon.on_shape.collidepoint(self.position):
                                self.light_minigame_on = True
                                self.light_minigame = Light_Minigame(self.screen, self.font, self.escale_img)
                                self.var_luz = -self.var_luz
                                if self.var_luz < 0:
                                    self.luz = True
                                    self.boton_luz_icon.need = 100
                                elif self.var_luz > 0:
                                    self.luz = False
                            if self.boton_soil_icon.off_shape.collidepoint(self.position) or self.boton_soil_icon.on_shape.collidepoint(self.position):
                                self.soil_minigame_on = True
                                self.soil_minigame = Soil_Minigame(self.screen, self.font, self.escale_img)
                                self.var_soil = -self.var_soil
                                if self.var_soil < 0:
                                    self.soil = True
                                    self.boton_soil_icon.need = 100
                                elif self.var_soil > 0:
                                    self.soil = False
                            if self.boton_temp_icon.off_shape.collidepoint(self.position) or self.boton_temp_icon.on_shape.collidepoint(self.position):
                                self.temp_minigame_on = True
                                self.temp_minigame = Temp_Minigame(self.screen, self.font, self.escale_img)
                                self.var_temp = -self.var_temp
                                if self.var_temp < 0:
                                    self.temp = True
                                    self.boton_temp_icon.need = 100
                                elif self.var_temp > 0:
                                    self.temp = False

                # Dejo de tener doble puntaje si dejo de apretar el boton
                if event.type == pygame.MOUSEBUTTONUP:
                    self.double_time = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.spacebar_pressed = True
                        print ('spacebar down')
                    self.pressed_letter = pygame.key.name(event.key).upper()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.spacebar_pressed = False
                        print ('spacebar up')
                

            # Termina el loop si algunos de los valores de necesidad de la planta bajan a 0 (pierdo)
            if self.boton_agua_icon.need <= 0 or self.boton_luz_icon.need <= 0 or self.boton_soil_icon.need <= 0 or self.boton_temp_icon.need <= 0:
                self.loop = False
            
            if self.water_minigame_on == True:
                self.exit_minigame = self.water_minigame.run()
                if (self.exit_minigame == 1):
                    self.water_minigame_on = False

            if self.light_minigame_on == True:
                self.exit_minigame = self.light_minigame.run(self.pressed_letter)
                self.pressed_letter = False
                if (self.exit_minigame == 1):
                    self.light_minigame_on = False

            if self.soil_minigame_on == True:
                self.exit_minigame = self.soil_minigame.run(self.mouse_pressed)
                self.mouse_pressed = False
                if (self.exit_minigame == 1):
                    self.soil_minigame_on = False

            if self.temp_minigame_on == True:
                self.exit_minigame = self.temp_minigame.run(self.spacebar_pressed)
                self.spacebar_pressed = False
                if (self.exit_minigame == 1):
                    self.temp_minigame_on = False
            
            pygame.display.update()
            self.clock.tick(c.FPS)