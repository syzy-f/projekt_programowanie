#sterowanie wsad oraz prędkość prototyp, do zaimplementowania ściąganie sterowanie z ustawień oraz prędkości z klasy postaci
import pygame
def controls(keys_pressed,player):
    keys = pygame.key.get_pressed()
    delta_x = 0
    delta_y = 0
    if keys[pygame.K_LEFT]:
        delta_x -= hero.speed
    if keys[pygame.K_RIGHT]:
        delta_x += hero.speed
    if keys[pygame.K_UP]:
        delta_y -= hero.speed
    if keys[pygame.K_DOWN]:
        delta_y += hero.speed
    if keys[pygame.K_ESCAPE]:
        running = False

        
# player = Hero(100, 100, speed=5)

    hero.move(delta_x, delta_y)
    window.fill(BACKGROUND_COLOR)
    hero.draw(window)

pygame.quit()

