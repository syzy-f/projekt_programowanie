import pygame, os, random
from main_variables import *

#klasy
class Item(pygame.sprite.Sprite):
    #podstawowe właściwości itemów
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = self.width
        self.height = self.height
        self.velocity = VEL
        #tor na którym zespawni się item
        self.lane = self.lane
        self.position_x = TOR_OFFSET + LANE_WIDTH // 2 + self.lane * (LANE_WIDTH + 97)
        self.position_y = -self.height
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.position_x, self.position_y)
        self.mask = pygame.mask.from_surface(self.image)
    #nowe funkcje
    
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
            self.kill()

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))
    #koniec nowych funkcji
    


            
class Hotdog(Item):
    def __init__(self,lane):
        #nadpisanie niektórych właściwości na potrzeby klasy hotdog
        self.lane = lane
        self.scale = 0.05
        self.width = self.scale*WIDTH
        self.height = self.scale*HEIGHT
        self.image = pygame.image.load(os.path.join('assets/items','hotdog.png'))
        super().__init__()
    def hotdog_collide(self,player):
        if pygame.sprite.collide_mask(player, self):
            if player.lives < 3:
                player.lives += 1

        
class Coffee(Item):
    #podstawowe właściwości itemów
    def __init__(self, lane):
        #nadpisanie niektórych właściwości na potrzeby klasy coffee
        self.lane = lane
        self.width = 0.05*WIDTH
        self.height = 0.07*HEIGHT
        self.image = pygame.image.load(os.path.join('assets/items','caffee.png'))
        super().__init__()
    def coffee_collide(self,player):
        if pygame.sprite.collide_mask(player, self):
            if player.speed < 45:
                player.speed += 3





    