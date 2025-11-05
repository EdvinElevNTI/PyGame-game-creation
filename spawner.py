import pygame
import random
import time
from enemy import Enemy1, Enemy2, Boss

round_num = 1
current_enemies = []

def spawn_enemies():
    # Calculate the amount of enemies
    amount_of_enemies = round_num*2 + 1
    
    # Spawn at least round_num - 1 of Enemy1, max amount_of_enemies - 1
    # Spawn the rest as Enemy2
    spawn_e1 = random.randint(1, amount_of_enemies-1)
    spawn_e2 = amount_of_enemies - spawn_e1

    # Every 3rd round: Spawn boss
    if round_num == 3:
        x = 0
        y = 0
        current_enemies.append(Boss(x, y))
    
    # If no Boss, spawn enemies
    else:
        # Add Enemy1 and Enemy2 to current_enemies
        for i in range(spawn_e1):
            x = random.randint(0, 800-50)  # random x position
            y = random.randint(0, 600-50)  # random y position
            current_enemies.append(Enemy1(x, y, "enemy1.png"))
        
        for i in range(spawn_e2):
            x = random.randint(0, 800-50)  # random x position
            y = random.randint(0, 600-50)  # random y position
            current_enemies.append(Enemy2(x, y, "enemy2.png"))


def update_enemy_status():
    # Make the variables global
    global current_enemies, round_num
    
    # Update the list to only contain living enemies
    current_enemies = [e for e in current_enemies if e.alive]

    # If there are no enemies left
    if not current_enemies:
        if round_num != 3:
            round_num += 1
            
            # Wait 2 seconds before spawning next round
            time.sleep(2)
            spawn_enemies()
        else:
            pass