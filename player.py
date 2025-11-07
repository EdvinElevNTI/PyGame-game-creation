import pygame

speed = 5
max_health = 250

class Player:
    def __init__(self, x, y):
        player_image = pygame.image.load("player.png").convert_alpha()
        self.image = player_image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.max_health = max_health #NEW
        self.health = max_health 
        self.attack_damage = 50  # NEW
        self.is_attacking = False
        self.attack_cooldown = 500
        self.last_attack_time = 0

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

    def attack(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        if keys[pygame.K_SPACE] and current_time - self.last_attack_time > self.attack_cooldown:
            self.is_attacking = True
            self.last_attack_time = current_time
            attack_rect = self.rect.inflate(300, 300)
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
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y - 10, self.rect.width, 5))
        pygame.draw.rect(screen, (0, 255, 0),
                         (self.rect.x, self.rect.y - 10, self.rect.width * (self.health / self.max_health), 5))
