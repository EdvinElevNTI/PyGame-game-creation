import pygame

max_health = 100

class Enemy:
    def __init__(self,enemy_x,enemy_y, image_path):
        self.x = enemy_x
        self.y= enemy_y
        self.alive = True
        self.health = max_health
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(enemy_x,enemy_y))
        self.is_attacking = False   # True då attackerar
        self.attack_cooldown = 500  # tiden (millisekunder) mellan attackerna (så ej spamm)
        self.last_attack_time = 0

    def enemy_movement(self, x, y, speed):
        if self.x > x:
            self.x -= speed
        elif self.x < x:
            self.x += speed
        
        if self.y > y:
            self.y -= speed
        elif self.y < y:
            self.y += speed

        self.rect.topleft = (self.x, self.y)
        return self.x, self.y
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

     # For the enemy to be able to die
    def is_dead(self):
        return self.health <= 0

    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
     # Draw health bar for enemy
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 10, self.rect.width, 5))  # RÖD: Full health bar
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y - 10, self.rect.width * (self.health / max_health), 5))  # GRÖN: Health left

    
    