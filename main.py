import pygame
import sys

from player import Player
from enemy import Enemy

# Initialize pygame
pygame.init()

# Create a window (width * height)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")


player = Player(400, 300)
# Spawn the enemy
enemy = Enemy(100, 200, "enemytest.png")


# Main loop
dead = False
while not dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    
    # Update player position
    player.move()
    attack_rect = player.attack()  # Kan redigera sen efter att fixat enemies

    # Update enemy location
    enemy_x, enemy_y = enemy.enemy_movement(player.rect.x, player.rect.y)

    # Draw
    screen.fill((0, 0, 0))
    player.draw(screen)
    enemy.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 60 FPS

# Exit logic
pygame.quit()
sys.exit()
