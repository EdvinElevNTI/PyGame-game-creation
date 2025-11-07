import pygame
import sys
import time

from player import Player
import spawner
import enemy as enemy_module

# Initialize pygame
pygame.init()
font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")

player = Player(400, 300)

round_cooldown = 2000
last_round_time = pygame.time.get_ticks()
spawner.spawn_enemies()

bg = pygame.image.load("bg.png")

# Game state, can be playing or choosing_upgrade
game_state = "playing"

#game over screen, called when player dies
def game_over():
    global player, game_state

    # Stoppa spelet och visa Game Over-skärm
    while True:
        screen.fill((0, 0, 0))

        title = font.render("GAME OVER", True, (255, 0, 0))
        score_text = font.render(f"Points: {enemy_module.points}", True, (255, 255, 255))
        round_text = font.render(f"Round: {spawner.round_num}", True, (255, 255, 255))
        restart_text = font.render("Press R to Restart or Q to Quit", True, (200, 200, 200))

        screen.blit(title, (300, 200))
        screen.blit(score_text, (330, 280))
        screen.blit(round_text, (330, 320))
        screen.blit(restart_text, (200, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
        elif keys[pygame.K_r]:
            restart_game()
            return  # lämnar game_over och fortsätter spelet igen
        
def restart_game():
    global player, spawner, enemy_module, game_state, last_round_time

    # Återställ variabler
    enemy_module.points = 0
    spawner.round_num = 1
    spawner.current_enemies.clear()

    player = Player(400, 300)  # ny spelare
    spawner.spawn_enemies()

    game_state = "playing"
    last_round_time = pygame.time.get_ticks()



def choose_upgrade():
    global game_state
    game_state = "choosing_upgrade"

def upgrade_menu(player):
    screen.fill((0, 0, 0))
    title = font.render("Choose an upgrade:", True, (255, 255, 255))
    screen.blit(title, (250, 200))

    opt1 = font.render("1 - Increase movement speed (+1)", True, (0, 255, 0))
    opt2 = font.render("2 - Increase max health (+10) and + 50hp", True, (0, 255, 0))
    opt3 = font.render("3 - Increase attack damage (+10)", True, (0, 255, 0))

    screen.blit(opt1, (250, 280))
    screen.blit(opt2, (250, 320))
    screen.blit(opt3, (250, 360))

    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        player.speed += 1
        return True
    elif keys[pygame.K_2]:
        player.health += 50
        player.max_health += 10
        return True
    elif keys[pygame.K_3]:
        player.attack_damage += 10
        return True

    return False

dead = False

# Main loop
while not dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True


    # screen.fill(0,0,0)
    screen.blit(bg, (0,0))

    # game state - playing
    if game_state == "playing":
        player.move()
        attack_rect = player.attack()

        # Enemy movement
        for enemy in spawner.current_enemies:
            enemy.enemy_movement(player.rect.x, player.rect.y)

        # Enemy attack
        for enemy in spawner.current_enemies:
            enemy.attack(player, pygame.time.get_ticks())

        # Player attack
        if attack_rect:
            for enemy in spawner.current_enemies:
                if enemy.rect.colliderect(attack_rect):
                    enemy.take_damage(player.attack_damage)

        # Remove dead enemies
        spawner.remove_dead_enemies()

        # Draw enemies
        for enemy in spawner.current_enemies:
            enemy.draw(screen)

        # Round logic
        if not spawner.current_enemies:
            choose_upgrade()

        # Draw player
        player.draw(screen)

    # playing state - upgrade
    elif game_state == "choosing_upgrade":
        if upgrade_menu(player):
            spawner.next_round()
            last_round_time = pygame.time.get_ticks()
            game_state = "playing"

    # UI elements
    points_text = font.render(f"Points: {enemy_module.points}", True, (255, 255, 255))
    screen.blit(points_text, (10, 10))

    round_text = font.render(f"Round: {spawner.round_num}", True, (255, 255, 255))
    screen.blit(round_text, (10, 560))

    if player.health <= 0:
        game_over()

    pygame.display.flip()
    pygame.time.Clock().tick(60)
