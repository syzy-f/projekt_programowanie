
import pygame
import os  # operating system



# stałe gry
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BORDER_WIDTH = 200
BORDER_HEIGHT = 400
HERO_SIZE = 128
FPS = 60    # 60 time per second, żeby na każdym kompie tak samo szybko się pojawiało

# kolor okna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)  # code for black - none of red, none of blue, none of green
BACKGROUND_COLOR = (244, 220, 181)      #jasny beż

# inicjalizacja pygame
pygame.init()
clock = pygame.time.Clock()


#utworzenie okna gry
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("BIMBA SURFERS GAME")


# Załadowanie obrazka potwora i skalowanie
HERO_IMAGE = pygame.image.load(os.path.join('Assets', 'hero.png'))  #os po to żeby auomatycznie działało na windowsie czy macu
HERO_IMAGE = pygame.transform.scale(HERO_IMAGE, (HERO_SIZE, HERO_SIZE))


# Utworzenie powierzchni z przezroczystością dla kwadratu wokół bohatera
rectangle_surface = pygame.Surface((HERO_SIZE, HERO_SIZE), pygame.SRCALPHA)
pygame.draw.rect(rectangle_surface, (0, 0, 0, 100), (0, 0, HERO_SIZE, HERO_SIZE))



class Hero:
    def __init__(self, x, y, speed = 5):
        self.x = x
        self.y = y
        self.speed = 0
        self.life_points = 100

    def move(self, delta_x, delta_y):

         # Aktualizacja pozycji bohatera
        self.x += delta_x
        self.y += delta_y

        # Ograniczenie bohatera do granic okna
        if self.x < 0:
            self.x = 0
        elif self.x > WINDOW_WIDTH - HERO_SIZE:
            self.x = WINDOW_WIDTH - HERO_SIZE
        if self.y < 0:
            self.y = 0
        elif self.y > WINDOW_HEIGHT - HERO_SIZE:
            self.y = WINDOW_HEIGHT - HERO_SIZE

    def draw(self, surface):
        # Narysowanie bohatera na podanej powierzchni
        surface.blit(HERO_IMAGE, (self.x, self.y))
       

# Utworzenie instancji potwora
hero = Hero(100, 100, speed=5)

# Główna pętla gry
running = True
while running:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Sterowanie bohaterem
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

    # Poruszanie potworem
    hero.move(delta_x, delta_y)

    # Wyczyszczenie ekranu
    window.fill(BACKGROUND_COLOR)

    # Rysowanie bohatera
    hero.draw(window)

    # Aktualizacja ekranu
    pygame.display.flip()

    clock.tick(FPS)

# Zamknięcie Pygame
pygame.quit()
