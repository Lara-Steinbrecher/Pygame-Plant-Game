import pygame

class Aguja():
    def __init__(self, x, y):
        self.aguja_stages = [
            pygame.image.load("assets//images//aguja//aguja12.png").convert_alpha(),
            pygame.image.load("assets//images//aguja//aguja1.png").convert_alpha(),
            pygame.image.load("assets//images//aguja//aguja2.png").convert_alpha(),
            pygame.image.load("assets//images//aguja//aguja3.png").convert_alpha(),
            pygame.image.load("assets//images//aguja//aguja4.png").convert_alpha(),
            pygame.image.load("assets//images//aguja//aguja5.png").convert_alpha(),
            pygame.image.load("assets//images//aguja//aguja6.png").convert_alpha(),
            pygame.image.load("assets//images//aguja//aguja7.png").convert_alpha(),
            pygame.image.load("assets//images//aguja//aguja8.png").convert_alpha(),
            pygame.image.load("assets//images//aguja//aguja9.png").convert_alpha(),
            pygame.image.load("assets//images//aguja//aguja10.png").convert_alpha(),
            pygame.image.load("assets//images//aguja//aguja11.png").convert_alpha()
        ]
        self.index = 0
        self.imagen = self.aguja_stages[self.index]
        self.mask = pygame.mask.from_surface(self.imagen)
        self.rect = self.imagen.get_rect(center=(x, y))

    def draw(self, screen):
        self.screen = screen
        self.imagen = self.aguja_stages[self.index]
        self.screen.blit(self.imagen, self.rect)

    def change_stage(self):
        self.index += 1
        if self.index >= 12:
            self.index = 0

class Agujita():
    def __init__(self, x, y):
        self.agujita_stages = [
            pygame.image.load("assets//images//agujita//aguja60.png").convert_alpha(),
            pygame.image.load("assets//images//agujita//agujita5.png").convert_alpha(),
            pygame.image.load("assets//images//agujita//agujita10.png").convert_alpha(),
            pygame.image.load("assets//images//agujita//agujita15.png").convert_alpha(),
            pygame.image.load("assets//images//agujita//agujita20.png").convert_alpha(),
            pygame.image.load("assets//images//agujita//agujita25.png").convert_alpha(),
            pygame.image.load("assets//images//agujita//agujita30.png").convert_alpha(),
            pygame.image.load("assets//images//agujita//agujita35.png").convert_alpha(),
            pygame.image.load("assets//images//agujita//agujita40.png").convert_alpha(),
            pygame.image.load("assets//images//agujita//agujita45.png").convert_alpha(),
            pygame.image.load("assets//images//agujita//agujita50.png").convert_alpha(),
            pygame.image.load("assets//images//agujita//agujita55.png").convert_alpha()
        ]
        self.index = 0
        self.imagen = self.agujita_stages[self.index]
        self.mask = pygame.mask.from_surface(self.imagen)
        self.rect = self.imagen.get_rect(center=(x, y))

    def draw(self, screen):
        self.screen = screen
        self.imagen = self.agujita_stages[self.index]
        self.screen.blit(self.imagen, self.rect)

    def change_stage(self):
        self.index += 1
        if self.index >= 12:
            self.index = 0

class Interruptor():
    def __init__(self, x, y):
        self.interruptor_stages = [
            pygame.image.load("assets//images//reloj_no_presionado.png").convert_alpha(),
            pygame.image.load("assets//images//reloj_presionado.png").convert_alpha()
        ]
        self.index = 0
        self.imagen = self.interruptor_stages[self.index]
        self.mask = pygame.mask.from_surface(self.imagen)
        self.rect = self.imagen.get_rect(center=(x, y))

    def draw(self, screen):
        self.screen = screen
        self.imagen = self.interruptor_stages[self.index]
        self.screen.blit(self.imagen, self.rect)

    def zero_state(self):
        self.index = 0
    def on_state(self):
        self.index = 1

    
    def check_collision(self, mouse_pos, mouse_mask):
        self.mouse_pos = mouse_pos
        self.mouse_mask = mouse_mask
        self.pos_difference = (self.mouse_pos[0] - self.rect.x, self.mouse_pos[1] - self.rect.y)
        if self.mask.overlap(self.mouse_mask, self.pos_difference):
            return 1