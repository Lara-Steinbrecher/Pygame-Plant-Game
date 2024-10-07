import pygame

# Initialize Pygame
pygame.init()

# Set up screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load an image and create a mask for it
image = pygame.image.load("assets//images//maceta.png")
masked = pygame.mask.from_surface(image)

# Get image dimensions and position
image_rect = image.get_rect()
image_rect.topleft = (300, 200)  # Position the object at (300, 200)

# Create a 1x1 pixel mask for the mouse (a point)
mouse_mask = pygame.mask.Mask((1, 1), fill=True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Calculate the offset between the mask and the mouse position
    # Offset is the difference between the object's rect position and the mouse position
    offset = (mouse_pos[0] - image_rect.x, mouse_pos[1] - image_rect.y)

    # Check if the object's mask overlaps with the 1x1 pixel mouse mask
    if masked.overlap(mouse_mask, offset):
        print("Mouse is on the object!")
    else:
        print("Mouse is not on the object.")

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit the image to the screen
    screen.blit(image, image_rect.topleft)

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
