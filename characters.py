import os
import pygame
from main_variables import WIN, WIDTH, HEIGHT


class Hero(pygame.sprite.Sprite):

    """Klasa gracza."""

    def __init__(self, speed=30):

        # Dziedziczymy z Sprite więc wywołuje jego kontruktor
        pygame.sprite.Sprite.__init__(self)

        # Wczytanie obrazka postaci
        self.hero_width = 220
        self.hero_height = 220

        # Inicjalizacja animacji
        # Lista przechowująca obrazy postaci dla animacji.
        self.animation_frames = []
        # Indeks aktualnej klatki animacji (aktualnie może być tylko 0 lub 1)
        self.current_frame = 0
        # Opóźnienie pomiędzy zmianami klatek animacji
        self.animation_delay = 10
        # Licznik zwiększany co wykonanie pętli
        self.animation_counter = 0

        # Wczytanie obrazków postaci
        image_1 = pygame.image.load(os.path.join('assets/characters', 'hero_1.png')).convert_alpha()
        image_2 = pygame.image.load(os.path.join('assets/characters', 'hero_2.png')).convert_alpha()
        image_3 = pygame.image.load(os.path.join('assets/characters', 'hero_3.png')).convert_alpha()

        # Skalowanie obrazków postaci
        image_1 = pygame.transform.scale(image_1, (self.hero_width, self.hero_height))
        image_2 = pygame.transform.scale(image_2, (self.hero_width, self.hero_height))
        image_3 = pygame.transform.scale(image_3, (self.hero_width, self.hero_height))

        # Dodanie obrazków do animacji
        self.animation_frames.append(image_1)
        self.animation_frames.append(image_2)
        self.animation_frames.append(image_3)

        # Ustawienie pierwszego obrazka jako początku animacji
        self.image = self.animation_frames[self.current_frame]
        self.mask = pygame.mask.from_surface(self.image)

        # Obrazki serc dla gracza
        # Wymiary
        self.heart_width = 30
        self.heart_height = 30

        # Obrazki i przeskalowanie
        self.hear_image = pygame.image.load(os.path.join('assets/characters', 'heart.png')).convert_alpha()
        self.hear_image = pygame.transform.scale(self.hear_image, (self.heart_width, self.heart_height))
        self.broken_heart_image = pygame.image.load(os.path.join('assets/characters', 'broken_heart.png')).convert_alpha()
        self.broken_heart_image = pygame.transform.scale(self.broken_heart_image, (self.heart_width, self.heart_height))

        # Utworzenie prostokąta gracza
        self.rect = self.image.get_rect()

        # Początkowe ustawienie gracza
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 5

        self.speed = speed
        self.lives = 3

        # przciski w zmiennych, aby możabyło zmieniać
        self.left = pygame.K_LEFT
        self.right = pygame.K_RIGHT

        # Miganie gracza po zderzeniu
        self.is_flickering = False
        self.flicker_duration = 45  # ok 1.5 sekundy
        self.flicker_counter = 0

    def decrease_life(self):
        # Aktualny czas mrugania zerujemy
        self.flicker_counter = 0
        # Gracz od teraz będzie mrugał
        self.is_flickering = True

    def hero_controls(self, keys_pressed):
        if keys_pressed[self.left] and self.rect.x > 0.340 * WIDTH:
            # wartość ograniczenia ruchu w lewo
            self.rect.x -= self.speed

        if keys_pressed[self.right] and self.rect.x < 0.515 * WIDTH:
            # wartość ograniczenia ruchu w prawo
            self.rect.x += self.speed

    def update_animation(self):
        # Zwiększamy wartość licznika animacji
        self.animation_counter += 1
        # Jeśli licznik animacji przekroczy czas pomiędzy zaminą klatek
        if self.animation_counter >= self.animation_delay:
            # Zerujemy licznik
            self.animation_counter = 0
            # Zmieniamy indeks aktualnej klatki na następną
            self.current_frame += 1
            # Jeśli indeks aktualnej klatki jest >= liczbie klatek to go zerujemy (przejście do pierwszej klatki)
            if self.current_frame >= len(self.animation_frames):
                self.current_frame = 0
            # Ustawienie nowego obrazka do rysowania
            self.image = self.animation_frames[self.current_frame]

    def hero_draw(self):
        if self.is_flickering:
            self.flicker_counter += 1
            if self.flicker_counter >= self.flicker_duration:
                self.is_flickering = False

        # Jeśli któryś z warunków jest prawidłowy to rysuj gracza
        # Jeśli nie miga lub jeśli miga, ale gdy aktualny licznik migania daje resztę z dzielania przez 15 < 8
        if not self.is_flickering or self.flicker_counter % 15 < 8:
            WIN.blit(self.image, (self.rect.x, self.rect.y))

    def show_lives(self):
        for i in range(self.lives):
            WIN.blit(self.hear_image, (35 + i * self.heart_width, 15, self.heart_height, self.heart_width))
        for i in range(3 - self.lives):
            WIN.blit(self.broken_heart_image, (35 + (self.lives + i) * self.heart_width, 15, self.heart_height, self.heart_width))

    def update(self, keys_pressed):
        self.update_animation()
        self.hero_controls(keys_pressed)
        self.hero_draw()
