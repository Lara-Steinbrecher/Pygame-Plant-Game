import pygame

class Object():
    def __init__(self, url, x, y):
        self.imagen = pygame.image.load(url).convert_alpha()
        self.mask = pygame.mask.from_surface(self.imagen)
        self.rect = self.imagen.get_rect(center=(x, y))

    def draw(self, screen):
        self.screen = screen
        self.screen.blit(self.imagen, self.rect)

    def check_collision(self, mouse_pos, mouse_mask):
        self.mouse_pos = mouse_pos
        self.mouse_mask = mouse_mask
        self.pos_difference = (self.mouse_pos[0] - self.rect.x, self.mouse_pos[1] - self.rect.y)
        if self.mask.overlap(self.mouse_mask, self.pos_difference):
            return 1
