import pygame
import random
from enemy import Enemy1, Enemy2, Boss

round_num = 1
current_enemies = []


def spawn_enemies():
    # Calculate the amount of enemies (+1 or +2):
    # 6, 8, 9, 11, 12, 14, 15, 17, 18, 20
    amount_of_enemies = ((round_num * 3) // 2) + 5
    
    # Spawn at least round_num + 1 of Enemy1, max amount_of_enemies - 2
    # Spawn the rest as Enemy2
    spawn_e1 = random.randint(round_num+3, amount_of_enemies-2)
    spawn_e2 = amount_of_enemies - spawn_e1

    # Every 3rd round: Spawn boss
    if round_num % 3 == 0:
        x = 0
        y = 0
        current_enemies.append(Boss(x, y))
    
    else:
        # Add Enemy1 and Enemy2 to current_enemies
        for i in range(0, spawn_e1):
            x = random.randint(0, 800-50)  # random x position
            y = random.randint(0, 600-50)  # random y position
            current_enemies.append(Enemy1(x, y))
        
        for i in range(0, spawn_e2):
            x = random.randint(0, 800-50)  # random x position
            y = random.randint(0, 600-50)  # random y position
            current_enemies.append(Enemy2(x, y))


def update_enemy_status():
    # Make the variables global
    global current_enemies, round_num
    
    # Update the list to only contain living enemies
    current_enemies = [e for e in current_enemies if e.alive]

    # If there are no enemies left
    if not current_enemies:
        round_num += 1