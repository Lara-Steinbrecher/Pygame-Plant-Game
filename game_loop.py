import pygame
import CONSTANTES as c
from objects.planta import Planta
import random
import sys
from minijuegos.light_minigame import Light_Minigame
from minijuegos.water_minigame import Water_Minigame
from minijuegos.soil_minigame import Soil_Minigame
from minijuegos.temp_minigame import Temp_Minigame
from objects.needs_paper import Needs_Paper
from objects.object import Object
from objects.clock import Aguja, Agujita, Interruptor
from objects.termostato import Termostato
from menu_music import background_music, win_sound, game_over_sound


class Game_Loop():
    def __init__(self, screen, font, escale_img, clock):
        self.clock = clock
        self.screen = screen
        self.font = font
        self.escale_img = escale_img

        self.background = pygame.image.load("assets//images//Background.png")

        self.agujita = Agujita(74, 80)
        self.aguja = Aguja(75, 80)
        self.pala = Object("assets//images//pala.png",48, 390)
        self.rastrillo = Object("assets//images//rastrillo.png",48, 390)
        self.planta = Planta(310, 235)
        self.notita = Object("assets//images//notita.png",200, 330)
        self.regadera = Object("assets//images//regadera.png", 500, 270)
        self.reloj_interruptor = Interruptor(90, 130)
        self.reloj_circle = Object("assets//images//reloj.png", 76, 80)

        self.termostat_detection = pygame.Surface((53, 35), pygame.SRCALPHA)
        self.termostat_rect_detection = self.termostat_detection.get_rect(center=(621, 320))
        self.termostato = Termostato(612, 317)
        
        self.window = pygame.Surface((140, 340), pygame.SRCALPHA)
        self.window_rect = self.window.get_rect(center=(218, 153))


        self.mouse_mask = pygame.mask.Mask((1, 1), fill=True)

        self.water_need = 100
        self.light_need = 100
        self.soil_need = 100
        self.temp_need = 100

        self.temp_need_tracker = 0

        # Timer
        self.MY_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.MY_EVENT, 1000) # cada 1 segundo
        self.reloj = c.TIEMPO
        # Cambia cuando estoy manteniendo el boton de acelerar tiempo
        self.double_time = False
        self.points = 0
        self.stage_tracker = 0
        self.clock_stage = 0
        self.miniclock_stage = 0
        

        # Variables que se activan cuando se activa un minigame
        self.water_minigame_on = False
        self.light_minigame_on = False
        self.soil_minigame_on = False
        self.temp_minigame_on = False
        self.needs_paper_on = False

        self.spacebar_pressed = False
        self.mouse_pressed = False
        self.pressed_letter = 0
        
        background_music()


    
    def run (self):
        self.loop = True
        while self.loop: 
            # Dibujo el fondo y todas las imagenes
            if self.double_time == True:
                self.reloj_interruptor.on_state()

            self.screen.blit(self.background,(0,0)) #fondo centrado

            self.pala.draw(self.screen)
            self.rastrillo.draw(self.screen)
            self.notita.draw(self.screen)
            self.regadera.draw(self.screen)
            self.screen.blit(self.termostat_detection, self.termostat_rect_detection)
            self.termostato.draw(self.screen)
            self.screen.blit(self.window, self.window_rect)
            self.reloj_interruptor.draw(self.screen)
            self.reloj_circle.draw(self.screen)
            self.planta.draw(self.screen)
            self.termostato.draw(self.screen)
            self.aguja.draw(self.screen) 
            self.agujita.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Timer, te da doble puntaje mientras lo mantengas presionado al boton
                if event.type == self.MY_EVENT:
                    if self.double_time == True:
                        self.reloj -= 1
                        self.points += 2
                        self.water_need -= random.randint (2, 4)
                        random_number = random.randint (2, 4)

                        self.light_need -= random.randint (2, 4)
                        self.soil_need -= random.randint (2, 4)
                        self.temp_need -= random_number
                        if self.clock_stage >= 1:
                            self.aguja.change_stage()
                            self.clock_stage = 0

                        if self.miniclock_stage >= 5:
                            self.agujita.change_stage()
                            self.miniclock_stage = 0
                        self.clock_stage += 1
                        self.miniclock_stage += 1
                        self.temp_need_tracker += random_number
                    else:
                        self.reloj -= 1
                        self.points += 1
                        self.water_need -= 1
                        self.light_need -= 1
                        self.soil_need -= 1
                        self.temp_need -= 1
                        if self.clock_stage >= 3:
                            self.aguja.change_stage()
                            self.clock_stage = 0

                        if self.miniclock_stage >= 15:
                            self.agujita.change_stage()
                            self.miniclock_stage = 0
                        self.clock_stage += 1
                        self.miniclock_stage += 1
                        self.temp_need_tracker += 1
                    
                    if self.stage_tracker == 30:
                        self.planta.change_stage()
                        self.stage_tracker = 0
                    else:
                        self.stage_tracker += 1


                # Si clickeo, me fijo cual boton es:
                #   Para el boton de skip, duplico el puntaje y para los demás le cambio entre estado on y off
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.position = pygame.mouse.get_pos()
                    print(self.position)
                    self.mouse_pressed = True

                    if self.water_minigame_on == False and self.light_minigame_on == False and self.soil_minigame_on == False and self.temp_minigame_on == False:
                        if event.button == 1:
                            if self.reloj_interruptor.check_collision(self.position, self.mouse_mask) == 1 or self.reloj_circle.check_collision(self.position, self.mouse_mask) == 1:
                                self.double_time = True
                            
                            # Comprobando colision con regadera
                            if self.regadera.check_collision(self.position, self.mouse_mask) == 1:
                                self.water_minigame_on = True
                                self.water_minigame = Water_Minigame(self.screen, self.font, self.escale_img)
                            if self.window_rect.collidepoint(self.position):
                                self.light_minigame_on = True
                                self.light_minigame = Light_Minigame(self.screen, self.font, self.escale_img)
                            if self.pala.check_collision(self.position, self.mouse_mask) == 1 or self.rastrillo.check_collision(self.position, self.mouse_mask) == 1:
                                self.soil_minigame_on = True
                                self.soil_minigame = Soil_Minigame(self.screen, self.font, self.escale_img)
                            if self.termostat_rect_detection.collidepoint(self.position):
                                self.temp_minigame_on = True
                                self.temp_minigame = Temp_Minigame(self.screen, self.font, self.escale_img)
                            if self.notita.check_collision(self.position, self.mouse_mask) == 1:
                                self.needs_paper_on = True
                                self.needs_paper = Needs_Paper(self.screen, self.font, self.escale_img)

                # Dejo de tener doble puntaje si dejo de apretar el boton
                if event.type == pygame.MOUSEBUTTONUP:
                    self.double_time = False
                    self.reloj_interruptor.zero_state()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.spacebar_pressed = True
                        print ('spacebar down')
                    self.pressed_letter = pygame.key.name(event.key).upper()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.spacebar_pressed = False
                        print ('spacebar up')
                
            if self.temp_need_tracker == 20:
                self.temp_need_tracker = 0
                self.termostato.change_stage()
            
            if self.water_minigame_on == True:
                self.exit_minigame = self.water_minigame.run()
                if (self.exit_minigame == 1 or self.exit_minigame == 2):
                    self.water_minigame_on = False
                    if self.exit_minigame == 1:
                        self.water_need = 100

            if self.light_minigame_on == True:
                self.exit_minigame = self.light_minigame.run(self.pressed_letter)
                self.pressed_letter = False
                if (self.exit_minigame == 1 or self.exit_minigame == 2):
                    self.light_minigame_on = False
                    if self.exit_minigame == 1:
                        self.light_need = 100

            if self.soil_minigame_on == True:
                self.exit_minigame = self.soil_minigame.run(self.mouse_pressed, self.mouse_mask)
                self.mouse_pressed = False
                if (self.exit_minigame == 1 or self.exit_minigame == 2):
                    self.soil_minigame_on = False
                    if self.exit_minigame == 1:
                        self.soil_need = 100

            if self.temp_minigame_on == True:
                self.exit_minigame = self.temp_minigame.run(self.spacebar_pressed, self.termostato.imagen)
                self.spacebar_pressed = False
                if (self.exit_minigame == 1 or self.exit_minigame == 2):
                    self.temp_minigame_on = False
                    if self.exit_minigame == 1:
                        self.temp_need = 100
                        self.termostato.reset_stage()
                
            if self.needs_paper_on == True:
                self.exit_minigame = self.needs_paper.run(self.water_need, self.light_need, self.temp_need,self.soil_need)
                if (self.exit_minigame == 1):
                    self.needs_paper_on = False

             # Termina el loop si algunos de los valores de necesidad de la planta bajan a 0 (pierdo)
            if self.water_need <= 0 or self.light_need <= 0 or self.light_need <= 0 or self.temp_need <= 0:
                game_over_sound()
                return 0, self.planta, self.points
            
            if self.reloj <= 0:
                win_sound()
                return 1, self.planta.imagen, self.points


            pygame.display.update()
            self.clock.tick(c.FPS)