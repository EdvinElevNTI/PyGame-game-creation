import pygame
import sys
import time

from player import Player
# from enemy import Enemy
# from spawner import spawn_enemies, remove_dead_enemies, next_round, current_enemies
import spawner
import enemy as enemy_module

# Initialize pygame
pygame.init()
font = pygame.font.Font(None, 36)

# Create a window (width * height)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")

player = Player(400, 300)


round_cooldown = 2000
last_round_time = pygame.time.get_ticks()
spawner.spawn_enemies()

bg = pygame.image.load("bg.png")

def game_over():
    pygame.quit()
    sys.exit()

dead = False

# Main loop
while not dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    
    # screen.fill(0,0,0)
    screen.blit(bg, (0,0))

    # Update player position
    player.move()
    attack_rect = player.attack()  # Kan redigera sen efter att fixat enemies

    # Enemy movement
    for enemy in spawner.current_enemies:
        enemy.enemy_movement(player.rect.x, player.rect.y)

    # Enemy attack
    for enemy in spawner.current_enemies:
        enemy.attack(player, pygame.time.get_ticks())

    # Attack
    if attack_rect:
        for enemy in spawner.current_enemies:
            if enemy.rect.colliderect(attack_rect):
                enemy.take_damage(50)

    # Remove dead enemies
    spawner.remove_dead_enemies()

    # Draw enemies
    for enemy in spawner.current_enemies:
        enemy.draw(screen)

    # Round logic
    if not spawner.current_enemies:
        current_time = pygame.time.get_ticks()
        if current_time - last_round_time > round_cooldown:
            spawner.next_round()
            last_round_time = current_time


    # Draw
    player.draw(screen)

    points_text = font.render(f"Points: {enemy_module.points}", True, (255, 255, 255))
    screen.blit(points_text, (10, 10))

    points_text = font.render(f"Round: {spawner.round_num}", True, (255, 255, 255))
    screen.blit(points_text, (10, 560))

    if player.health <= 0:
        game_over()



    # End of loop
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 60 FPS
