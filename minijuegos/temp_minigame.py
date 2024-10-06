import pygame
import CONSTANTES as c

class Temp_Minigame():
    def __init__(self, screen, font, escale_img):
        self.screen = screen
        self.font = font
        self.escale_img = escale_img

        self.background = pygame.Surface(c.TEMP_BACKGROUND)
        self.background.fill('black')
        self.background_rect = self.background.get_rect(center = c.CENTER)

        self.bar = pygame.Surface((350,20))
        self.bar.fill('blue')
        self.bar_rect = self.bar.get_rect(center = c.CENTER)

        self.selector = pygame.Surface(c.SELECTOR_SURFACE)
        self.selector.fill('orange')

        self.objective = pygame.Surface((20,20))
        self.objective.fill('green')
        self.objective_rect = self.objective.get_rect(center = c.CENTER)

        self.error = pygame.Surface((10,20))
        self.error.fill('red')
    
        self.selector_speed = c.SELECTOR_SPEED
        self.selector_x = c.CENTER[0]
        
        self.on_objective = False
        self.error_x = 0
        self.spacebar_pressed= False
        self.spacebar_tracker = 1

    def run(self, spacebar_pressed):
        self.spacebar_pressed = spacebar_pressed
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.bar, self.bar_rect)
        self.screen.blit(self.selector, (self.selector_x, c.SELECTOR_Y))
        self.screen.blit(self.objective, self.objective_rect)

        self.selector_x += self.selector_speed

        # Si el selector se encuentra al borde de la barra invierte el sentido en el se mueve
        # El menos 20 es porque toma desde el borde izquierdo del selector para ver si coincide con la barra
        if self.selector_x >= (self.bar_rect.topright[0] - c.SELECTOR_SURFACE[0]) or self.selector_x <= self.bar_rect.topleft[0]:
            self.selector_speed = -self.selector_speed
        
        if self.selector_x < self.objective_rect.topright[0] and self.selector_x > self.objective_rect.topleft[0]:
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
            self.screen.blit(self.error, (self.error_x, c.ERROR_Y))