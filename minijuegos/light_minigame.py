import pygame
import CONSTANTES as c
import random
import string

class Light_Minigame():
    def __init__(self, screen, font, escale_img):
        self.screen = screen
        self.font = font
        self.escale_img = escale_img

        self.background = pygame.Surface((450,300))
        self.background.fill('black')
        self.background_rect = self.background.get_rect(center = (c.ANCHO // 2, c.ALTO // 2))

        # Mezclo y tomo 8 de un array de letras
        self.letters = list(string.ascii_uppercase)
        self.letters = random.sample(self.letters,8)
        self.center_index = 0

        self.pressed_letter = 0

        self.spacing = -100
        self.smaller_letter_scale = 0.5
        self.small_font = pygame.font.SysFont("Arial", 12)

    
    def run(self, pressed_letter):
        self.screen.blit(self.background, self.background_rect)
        self.center_letter = self.letters[self.center_index]
        self.pressed_letter = pressed_letter

        ### Center Letter ###
        text_surface = self.font.render(self.center_letter, True, 'white')
        text_rect = text_surface.get_rect(center=(c.ANCHO // 2, c.ALTO // 2))
        self.screen.blit(text_surface, text_rect)
        
        ### Right letters ###
        for i in range(self.center_index - 1, max(-1, self.center_index - 3), -1):
            letter = self.letters[i]
            text = self.small_font.render(letter, True, 'gray')
            text_rect = text.get_rect(center=(c.ANCHO // 2 + (i - self.center_index) * self.spacing, c.ALTO // 2))
            self.screen.blit(text, text_rect)

        ### Left letters ###
        for i in range(self.center_index + 1, min(self.center_index + 3, len(self.letters))):
            letter = self.letters[i]
            text = self.small_font.render(letter, True, 'gray')
            text_rect = text.get_rect(center=(c.ANCHO // 2 + (i - self.center_index) * self.spacing, c.ALTO // 2))
            self.screen.blit(text, text_rect)

        if self.pressed_letter == self.letters[self.center_index]:
            self.center_index += 1  # Move to the next letter

            # Wrap around if we reach the end
            if self.center_index >= len(self.letters):
                return 1
        elif self.pressed_letter != 0:
            self.center_index = 0
            self.letters = list(string.ascii_uppercase)
            self.letters = random.sample(self.letters,8)