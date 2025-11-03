import pygame


class Enemy:
    def __init__(self,enemy_x,enemy_y):
        self.x = enemy_x
        self.y= enemy_y
        self.alive = True

    def enemy_movement(self, x, y, speed=2):
        if self.x > x:
            self.x -= speed
        elif self.x < x:
            self.x += speed
        
        if self.y > y:
            self.y -= speed
        elif self.y < y:
            self.y += speed
        return self.x, self.y
    
    