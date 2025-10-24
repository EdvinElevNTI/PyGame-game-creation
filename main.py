import pygame
import sys

from player import player, player_movement

# Initialize pygame
pygame.init()

# Create a window (width * height)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")


def add_player_at_location(x, y):
    screen.blit(player, (x, y))


x = 800 * 0.5
y = 600 * 0.5

# Main loop
dead = False
while not dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    
    # Update player position
    x, y = player_movement(x, y)

    # Draw
    screen.fill((0, 0, 0))
    add_player_at_location(x, y)
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 60 FPS

# Exit logic
pygame.quit()
sys.exit()