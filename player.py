import pygame

player = pygame.image.load('player.png')

speed = 7

def player_movement(x, y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 800 - player.get_width():
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < 600 - player.get_height():
        y += speed
    return x, y