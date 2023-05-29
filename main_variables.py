import pygame, os
    #zmienne gry
#fpsy
FPS = 60
#szybkość ekranu/itemów/wszystkiego
VEL = 30
#grupa wszystkich obiektów
all_sprites = pygame.sprite.Group()
#grupa wszystkich przeszkód
obstacles = pygame.sprite.Group()
#kontrolowanie odświeżania ekranu
clock = pygame.time.Clock()

    #zmienne okna

#szerokość okna
WIDTH = 1600
#wysokość okna
HEIGHT = 900
#tło ona
WHITE = (255,255,255)
#okno
background = pygame.image.load(os.path.join('assets/background','background.png'))
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#zmienne lini

LANE_WIDTH = (WIDTH - 4 * 390) // 3  # Szerokość pojedynczego pasa ruchu
TOR_OFFSET = (WIDTH - (3 * LANE_WIDTH + 2 * 105)) // 2  # Przesunięcie toru względem lewej krawędzi. Te 105 to moja zabawa pikselami, może to trzeba będzie usunąć
MIN_DISTANCE_BETWEEN_OBSTACLES = 500  # Minimalna odległość między przeszkodami. 500 jest chyba optymalne, od 400 i mniej gra może stać się niemożliwa do przejścia. Można tego używać do manipulowania poziomem trudności.

