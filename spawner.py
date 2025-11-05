import pygame
import random
import time
from enemy import Enemy

round_num = 1
current_enemies = []

def spawn_enemies():
    # Calculate the amount of enemies
    # amount_of_enemies = round_num*2 + 1
    amount_of_enemies = (round_num*3)//2 + 2
    
    # Spawn at least round_num - 1 of Enemy1, max amount_of_enemies - 1
    # Spawn the rest as Enemy2
    spawn_e1 = random.randint(1, amount_of_enemies-1)
    spawn_e2 = amount_of_enemies - spawn_e1

    # Every 3rd round: Spawn boss
    if round_num % 3 == 0:
        # Enemy(x, y, img, hp, dmg, speed)
        current_enemies.append(Enemy(0, 0, "boss.png", 800, 35, 3.5))
    
    # Add Enemy1 and Enemy2 to current_enemies
    for i in range(spawn_e1):
        x = random.randint(-100, 1000-50)  # random x position
        y = random.randint(-100, 800-50)  # random y position

        # Enemy(x, y, img, hp, dmg, speed)
        current_enemies.append(Enemy(x, y, "enemy1.png", 150, 10, 3))
        
    for i in range(spawn_e2):
        x = random.randint(-100, 1000-50)  # random x position
        y = random.randint(-100, 1000-50)  # random y position
        current_enemies.append(Enemy(x, y, "enemy2.png", 250, 20, 2))


def remove_dead_enemies():
    global current_enemies
    current_enemies = [e for e in current_enemies if e.alive]

def next_round():
    global round_num
    round_num += 1
    spawn_enemies()