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
    attack_rect = player.attack()
    
    # To be able to attack the enemy and for it to take damage
    if attack_rect and enemy.rect.colliderect(attack_rect) and not enemy.is_dead():
        enemy.take_damage(10)
        if enemy.is_dead():
            enemy.alive = False

    # Update enemy location
    enemy.enemy_movement(player.rect.x, player.rect.y)

    # Draw
    screen.fill((0, 0, 0))
    player.draw(screen)
    enemy.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 60 FPS

# Exit logic
pygame.quit()
sys.exit()
