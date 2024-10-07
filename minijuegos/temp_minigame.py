import pygame
import CONSTANTES as c

class Temp_Minigame():
    def __init__(self, screen, font, escale_img):
        self.screen = screen
        self.font = font
        self.escale_img = escale_img

        self.background = pygame.image.load("assets//images//Minijuego-temperatura-fondo.png").convert_alpha()
        self.background_rect = self.background.get_rect(center = c.CENTER)

        self.border = pygame.Surface((460, 310))
        self.border.fill('black')
        self.border_rect = self.border.get_rect(center = c.CENTER)

        self.bar = pygame.image.load("assets//images//Minijuego-temperatura-barra.png").convert_alpha()
        self.bar_rect = self.bar.get_rect(center = c.CENTER)

        self.selector = pygame.image.load("assets//images//Minijuego-temperatura-flecha-movimiento.png").convert_alpha()

        self.objective = pygame.image.load("assets//images//Minijuego-temperatura-acierto.png").convert_alpha()
        self.objective_rect = self.objective.get_rect(center = c.CENTER)

        self.error = pygame.image.load("assets//images//Minijuego-temperatura-fallo.png").convert_alpha()
    
        self.selector_speed = c.SELECTOR_SPEED
        self.selector_x = c.SELECTOR_X
        
        self.on_objective = False
        self.error_x = 0
        self.spacebar_pressed= False
        self.spacebar_tracker = 1

    def run(self, spacebar_pressed, termostato_imagen):
        self.spacebar_pressed = spacebar_pressed
        self.termostato_imagen = pygame.transform.scale_by(termostato_imagen,6)
        
        self.screen.blit(self.border,self.border_rect)
        self.screen.blit(self.background, self.background_rect)
        self.selector_rect = self.selector.get_rect(center=(self.selector_x, c.SELECTOR_Y))
        self.screen.blit(self.bar, self.bar_rect)
        self.screen.blit(self.selector, self.selector_rect)
        self.screen.blit(self.objective, self.objective_rect)
        self.screen.blit(self.termostato_imagen, (180,110))

        self.selector_x += self.selector_speed

        # Si el selector se encuentra al borde de la barra invierte el sentido en el se mueve
        # El menos 20 es porque toma desde el borde izquierdo del selector para ver si coincide con la barra
        if self.selector_x >= 530 or self.selector_x <= 180:
            self.selector_speed = -self.selector_speed
        
        if self.selector_x <= 375 and self.selector_x > 350:
            self.on_objective = True
        else:
            self.on_objective = False

        if self.spacebar_pressed == True and self.spacebar_tracker == 0:
            if self.on_objective == True:
                return 1
            else:
                self.error_x = self.selector_x
                self.spacebar_tracker = 1
        elif self.spacebar_pressed == False:
            self.spacebar_tracker = 0


        if self.error_x != 0:
            self.error_rect = self.error.get_rect(center=(self.error_x + 133,c.ERROR_Y))
            self.screen.blit(self.error, self.error_rect)

        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_ESCAPE]:
            return 2