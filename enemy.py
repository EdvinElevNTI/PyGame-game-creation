import pygame

points = 0

class Enemy:
    def __init__(self,enemy_x,enemy_y, image_path, hp, damage, speed):
        self.x = enemy_x
        self.y= enemy_y
        self.alive = True
        self.init_health = hp
        self.health = hp
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(enemy_x,enemy_y))
        self.speed = speed
        
        # Attack
        self.is_attacking = False   # True då attackerar
        self.attack_cooldown = 1500  # tiden (millisekunder) mellan attackerna (så ej spamm)
        self.last_attack_time = 0
        self.damage = damage

    def enemy_movement(self, x, y):
        if self.x > x:
            self.x -= self.speed
        elif self.x < x:
            self.x += self.speed
        
        if self.y > y:
            self.y -= self.speed
        elif self.y < y:
            self.y += self.speed

        self.rect.topleft = (self.x, self.y)

        return self.x, self.y
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            global points
            points += 10
            self.health = 0
            self.alive = False

    # For the enemy to be able to die
    def is_dead(self):
        return self.health <= 0
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # Draw health bar for enemy
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 10, self.rect.width, 5))  # RÖD: Full health bar
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y - 10, self.rect.width * (self.health / self.init_health), 5))  # GRÖN: Health left
    
    def attack(self, player, time):
        #check if enemy object collides with player obj 
        if self.rect.colliderect(player.rect):
            #deal damage to the player if time has passed since  last attack
            if time - self.last_attack_time >= self.attack_cooldown:
                player.take_damage(self.damage)
                # Update the time so the enemy waits for the next attack
                self.last_attack_time = time