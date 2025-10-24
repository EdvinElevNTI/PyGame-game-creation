import pygame
import sys

# Initialize all imported pygame modules
pygame.init()

# Create a window (width x height)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background (optional, just to clear screen)
    screen.fill((0, 0, 0))
    pygame.display.flip()  # Update the display

# Clean up
pygame.quit()
sys.exit()