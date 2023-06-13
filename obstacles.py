import os
import pygame
import random
from items import Item
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

    def item_collide(self, player):
        # Metoda collide_mask aktualizuje pozycję maski podczas wywoływania
        # I sprawdza czy nie doszło do kolizji dla wywoływanych obiektów
        if pygame.sprite.collide_mask(player, self):
            # Ta przeszkoda zawsze odbiera życie
            player.decrease_life()
            self.kill()

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Train(Item):
    """Klasa Train"""
    def __init__(self, lane):
        #nadpisanie niektórych właściwości na potrzeby klasy train
        self.lane = lane
        self.width = 0.062*WIDTH
        self.height = 0.38*HEIGHT
        self.image = pygame.image.load(os.path.join('assets/obstacles','train.png'))
        super().__init__()
    def train_collide(self,player):
        if pygame.sprite.collide_mask(player, self):
            player.decrease_life()


class Fans(Item):
    """Klasa Fans"""
    def __init__(self, lane):
        #nadpisanie niektórych właściwości na potrzeby klasy fans
        self.lane = lane
        self.width = 0.07*WIDTH
        self.height = 0.11*HEIGHT
        self.image = pygame.image.load(os.path.join('assets/obstacles','fans.png'))
        super().__init__()
    def fans_collide(self,player):
        if pygame.sprite.collide_mask(player, self):
            player.decrease_life()

