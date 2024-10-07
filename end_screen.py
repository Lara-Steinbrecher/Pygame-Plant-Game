import pygame
import CONSTANTES as c

class End_Screen():
    def __init__(self, points, screen, font, escale_img, clock):
        self.clock = clock
        self.screen = screen
        self.font = font
        self.escale_img = escale_img
        self.points = points
        
        # Initialize the background surface
        self.background = pygame.Surface((450, 300))
        self.background.fill('brown')

        # Start the background Y-coordinate above the screen (outside of view)
        self.background_x = (c.ANCHO // 2) - (self.background.get_width() // 2)
        self.background_y = -self.background.get_height()  # Start just outside the top

        self.target_y = (c.ALTO // 2) - (self.background.get_height() // 2)  # Center Y position
        self.animation_speed = 10  # Speed of the animation
        
    def run(self):
        self.loop = True
        while self.loop:
            self.screen.fill('black')
            
            # Move the background down until it reaches the center
            if self.background_y < self.target_y:
                self.background_y += self.animation_speed
                if self.background_y > self.target_y:
                    self.background_y = self.target_y  # Stop at the center

            # Draw the background surface
            self.screen.blit(self.background, (self.background_x, self.background_y))
            
            pygame.display.flip()  # Update the screen

            # Event handling (simplified)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop = False

            self.clock.tick(60)  # Limit the frame rate to 60 FPS