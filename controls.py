#sterowanie wsad oraz prędkość prototyp, do zaimplementowania ściąganie sterowanie z ustawień oraz prędkości z klasy postaci
import pygame
def controls(keys_pressed,player):
    UP = pygame.K_w
    DOWN = pygame.K_s
    LEFT = pygame.K_a
    RIGHT = pygame.K_d
    global VEL
    VEL = 100
    if keys_pressed[UP]:
        player.y-=VEL
    if keys_pressed[DOWN]:
        player.y+=VEL
    if keys_pressed[LEFT]:
        player.x-=VEL
    if keys_pressed[RIGHT]:
        player.x+=VEL