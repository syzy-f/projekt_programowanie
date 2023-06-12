import os
import pygame
import random

from characters import Hero
from main_variables import WIDTH, HEIGHT, TOR_OFFSET, LANE_WIDTH


class Bonus(pygame.sprite.Sprite):
    """Klasa ogólna bonusów"""
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

    def item_collide(self, player):
        if pygame.sprite.collide_mask(player, self):
            player.increase_life()
            self.kill()

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Hotdog(Bonus):
    """Klasa Hotdog."""

    def __init__(self, lane):
        path = os.path.join('assets/bonuses', 'hotdog.png')
        scale = 0.05
        width = scale * WIDTH
        height = scale * HEIGHT
        super().__init__(path=path, width=width, height=height)

        # Utworzenie maski do kolizji
        self.mask = pygame.mask.from_surface(self.image)
        # Ustalenie położenia na wybranym torze i przesunięcie obiektu
        self.set_lane(lane)

        print(f"Hotdog pozycja startowa: {self.position_x, self.position_y} - tor {self.lane})")

    def item_collide(self, player: Hero):
        if pygame.sprite.collide_mask(player, self):
            print("Got one live")
            player.increase_life()
            self.kill()


class Coffee(Bonus):
    """Klasa Coffee."""

    def __init__(self, lane):
        path = os.path.join('assets/bonuses', 'coffee.png')
        width = 0.05 * WIDTH
        height = 0.07 * HEIGHT
        super().__init__(path, width=width, height=height)

        self.mask = pygame.mask.from_surface(self.image)

        # Ustalenie położenia na wybranym torze i przesunięcie obiektu
        self.set_lane(lane)

        print(f"Coffee pozycja startowa: {self.position_x, self.position_y} - tor {self.lane})")

    def item_collide(self, player: Hero):
        if pygame.sprite.collide_mask(player, self):
            print("Got one live")
            player.increase_life()
            self.kill()
