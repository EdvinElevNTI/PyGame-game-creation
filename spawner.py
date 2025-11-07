import random
from enemy import Enemy

# Keep track of amount of rounds
round_num = 1

# List of enemies to spawn on a new round
current_enemies = []

# Decide what enemies to spawn (add to list)
def spawn_enemies():
    # Calculate the amount of enemies (2, 4, 5, 7, 8, 10, ...)
    amount_of_enemies = (round_num*3)//2 + 1 
    
    # Every 3rd round: Spawn boss
    if round_num % 3 == 0:
        # Enemy(x, y, img, hp, dmg, speed)
        current_enemies.append(Enemy(0, 0, "boss.png", 800, 30, 3.5))

        # decrease amount of enemies that spawn this round
        amount_of_enemies //= 2
    
    # Randomize the amount of each enemy
    spawn_e1 = random.randint(1, amount_of_enemies-1)
    spawn_e2 = amount_of_enemies - spawn_e1

    # Add enemy1 to current_enemies with randomized position
    for i in range(spawn_e1):
        x = random.randint(-100, 1000-50)  # random x position
        y = random.randint(-100, 800-50)  # random y position

        # Enemy(x, y, img, hp, dmg, speed)
        current_enemies.append(Enemy(x, y, "enemy1.png", 150, 7.5, 3))

    # Add enemy2 to current_enemies with randomized position
    for i in range(spawn_e2):
        x = random.randint(-100, 1000-50)  # random x position
        y = random.randint(-100, 1000-50)  # random y position
        current_enemies.append(Enemy(x, y, "enemy2.png", 250, 15, 2))

# Update current_enemeis to only include objects with alive = True
def remove_dead_enemies():
    global current_enemies
    current_enemies = [e for e in current_enemies if e.alive]

# Increase round num with 1, decide what enemies to spawn
def next_round():
    global round_num
    round_num += 1
    spawn_enemies()