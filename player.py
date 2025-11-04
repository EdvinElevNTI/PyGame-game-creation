import pygame

speed = 7               # player moves with speed 7
max_health = 100        # the total health is 100 (start)

class Player:
    def __init__(self, x, y):
        player_image = pygame.image.load('player.png').convert_alpha()
        self.image = player_image
        self.rect = self.image.get_rect(center=(x, y))  # lagrar players position och storlek
        self.speed = speed
        self.health = max_health
        self.is_attacking = False   # True då attackerar, annars false
        self.attack_cooldown = 500  # tiden (millisekunder) mellan attackerna (så ej spamm)
        self.last_attack_time = 0   # lagrar senaste atacken (cooldown)

    # Players movement
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 800 - self.rect.width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 600 - self.rect.height:
            self.rect.y += self.speed

    # Players attack
    def attack(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        # Tryck space för att attackera
        if keys[pygame.K_SPACE] and current_time - self.last_attack_time > self.attack_cooldown:    # Tillräckligt lång tid sedan förra attacken gått
            self.is_attacking = True
            self.last_attack_time = current_time
            
            # Return an attack hitbox
            attack_rect = self.rect.inflate(40, 40)  # Attack range, förstorar områden runt playern (representerar hitboxen)
            return attack_rect
        else:
            self.is_attacking = False
            return None

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_dead(self):
        return self.health <= 0

    def draw(self, screen):
        # Draw player
        screen.blit(self.image, self.rect)

        # Draw health bar
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y - 10, self.rect.width, 5))  # RÖD: Full health bar
        pygame.draw.rect(screen, (0, 255, 0),
                         (self.rect.x, self.rect.y - 10, self.rect.width * (self.health / max_health), 5))  # GRÖN: Health left

