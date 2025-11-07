import pygame

speed = 5           # The players speed
max_health = 250    # The players maximum health

class Player:
    def __init__(self, x, y):
        player_image = pygame.image.load("player.png").convert_alpha()  # Player sprite
        self.image = player_image
        self.rect = self.image.get_rect(center=(x, y))  # Position of the player
        self.speed = speed
        self.max_health = max_health
        self.health = max_health
        self.attack_damage = 50  # How much damage is taken when attacked
        self.is_attacking = False   # Is set to true when attacking
        self.attack_cooldown = 500  # To prevent from attack spam
        self.last_attack_time = 0

    def move(self):     # The players movement
        keys = pygame.key.get_pressed()   # Uses arrow keys

        if keys[pygame.K_LEFT] and self.rect.x > 0: # Left arrow key makes the player sprite (rect) go left etc
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 800 - self.rect.width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 600 - self.rect.height:
            self.rect.y += self.speed

    def attack(self):       # Making the player able to attack
        keys = pygame.key.get_pressed()     #by using the spacebar
        current_time = pygame.time.get_ticks()  # To prevent spam (also see line 35-37)

        if keys[pygame.K_SPACE] and current_time - self.last_attack_time > self.attack_cooldown:
            self.is_attacking = True
            self.last_attack_time = current_time
            attack_rect = self.rect.inflate(300, 300)   # The attack area
            return attack_rect
        else:
            self.is_attacking = False
            return None

    def take_damage(self, amount):  
        self.health -= amount       # Decreases the maximum health (when attacked by an enemy)
        if self.health < 0:
            self.health = 0

    def is_dead(self):      
        return self.health <= 0     # When health is empty the player is dead

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y - 10, self.rect.width, 5)) # RED healthbar for how much attacked
        pygame.draw.rect(screen, (0, 255, 0),
                         (self.rect.x, self.rect.y - 10, self.rect.width * (self.health / self.max_health), 5))     # GREEN Healthbar for health left (decreases)
