import pygame
import sys

from player import Player

# Initialize pygame
pygame.init()

# Create a window (width * height)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")


player = Player(400, 300)

# Main loop
dead = False
while not dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    
    # Update player position
    player.move()
    attack_rect = player.attack()  # Kan redigera sen efter att fixat enemies

    # Draw
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 60 FPS

# Exit logic
pygame.quit()
sys.exit()