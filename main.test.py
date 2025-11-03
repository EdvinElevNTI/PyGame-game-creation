import pygame
import sys

from player import player, player_movement
from enemy import Enemy

# Initialize pygame
pygame.init()

# Create a window (width * height)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")


def add_player_at_location(x, y):
    screen.blit(player, (x, y))

# Spawn the enemy
enemy = Enemy(100, 200)
# Img for enemy
enemy_img = pygame.image.load('Pygame\enemytest.png')

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

    # Update enemy location
    enemy_x, enemy_y = enemy.enemy_movement(x,y)

    # Draw
    screen.fill((0, 0, 0))
    add_player_at_location(x, y)
    screen.blit(enemy_img, (enemy.x, enemy.y))
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 60 FPS

# Exit logic
pygame.quit()
sys.exit()

