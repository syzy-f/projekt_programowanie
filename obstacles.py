import os
import pygame
import random

from characters import Hero
from main_variables import WIDTH, HEIGHT, TOR_OFFSET, LANE_WIDTH


class Obstacle(pygame.sprite.Sprite):
    """Klasa ogólna przeszkody"""
    def __init__(self, path, lane=1, width=50, height=50, velocity=30):
        pygame.sprite.Sprite.__init__(self)

        # Podstawowe właściwości itemów
        self.width = int(width)
        self.height = int(height)
        self.velocity = velocity

        self.path = path
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.lane = lane
        self.position_x = int(TOR_OFFSET + LANE_WIDTH // 2 + self.lane * (LANE_WIDTH + 97))
        self.position_y = int(-self.height)

        self.rect = self.image.get_rect()
        self.rect.center = (self.position_x, self.position_y)
        self.mask = pygame.mask.from_surface(self.image)

    def move_rect(self):
        self.rect.center = (self.position_x, self.position_y)

    def set_lane(self, lane):
        self.lane = lane
        self.position_x = TOR_OFFSET + LANE_WIDTH // 2 + self.lane * (LANE_WIDTH + 97)
        self.position_y = -self.height
        # Po przeliczeniu położenia na torze przesuń obiekt w jego miejsce
        self.move_rect()

    def update(self):
        self.rect.y += self.velocity
        if self.rect.top > HEIGHT:
            self.kill()

    def item_collide(self, player: Hero):
        # Metoda collide_mask aktualizuje pozycję maski podczas wywoływania
        # I sprawdza czy nie doszło do kolizji dla wywoływanych obiektów
        if pygame.sprite.collide_mask(player, self):
            # Ta przeszkoda zawsze odbiera życie
            player.decrease_life()
            self.kill()

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Train(Obstacle):
    """Klasa Train"""
    def __init__(self, lane):
        path = os.path.join('../../../Desktop/project_juki-main/assets', 'obstacles', 'train.png')
        width = 0.062 * WIDTH
        height = 0.38 * HEIGHT

        super().__init__(path=path, width=width, height=height)

        # Utworzenie maski do kolizji
        self.mask = pygame.mask.from_surface(self.image)
        # Ustalenie położenia na wybranym torze i przesunięcie obiektu
        self.set_lane(lane)

        print(f"Train pozycja startowa: {self.position_x, self.position_y} - tor {self.lane})")


class Fans(Obstacle):
    """Klasa Fans"""
    def __init__(self, lane):
        path = os.path.join('../../../Desktop/project_juki-main/assets', 'obstacles', 'fans.png')
        width = int(0.07 * WIDTH)
        height = int(0.11 * HEIGHT)
        super().__init__(path=path, width=width, height=height)

        # Utworzenie maski do kolizji
        self.mask = pygame.mask.from_surface(self.image)
        # Ustalenie położenia na wybranym torze i przesunięcie obiektu
        self.set_lane(lane)

        print(f"Fans pozycja startowa: {int(self.position_x), self.position_y} - tor {self.lane})")

