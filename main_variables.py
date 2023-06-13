import os
import pygame
import sys

# FPS'y
FPS = 60
# Szybkość ekranu/itemów/wszystkiego
VEL = 30

# Grupa wszystkich obiektów na torach
track_obstacles = pygame.sprite.Group()
# Kontrolowanie odświeżania ekranu
clock = pygame.time.Clock()


# Zmienne okna
# Szerokość okna
WIDTH = 1600
# Wysokość okna
HEIGHT = 900
# Okno
background = pygame.image.load(os.path.join('assets/background', 'background.png'))
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

# Zmienne lini
LANE_WIDTH = (WIDTH * 0.025) // 3  # Szerokość pojedynczego pasa ruchu
TOR_OFFSET = (WIDTH - (3 * LANE_WIDTH + 2 * 105)) // 2  # Przesunięcie toru względem lewej krawędzi. Te 105 to moja zabawa pikselami, może to trzeba będzie usunąć
MIN_DISTANCE_BETWEEN_OBSTACLES = 500  # Minimalna odległość między przeszkodami. 500 jest chyba optymalne, od 400 i mniej gra może stać się niemożliwa do przejścia. Można tego używać do manipulowania poziomem trudności.

# Kolory
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Poziomy trudności

obstacle_item_ratio = 0.8

def difficulty_level (level):
    if level == "easy":
        obs = 0.4 
    elif level =="medium":
        obs = 0.6
    elif level == "hard":
        obs = 0.8
    return obs