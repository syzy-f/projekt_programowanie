import pygame, os
from main_variables import WIN, WIDTH, HEIGHT, LANE_WIDTH, TOR_OFFSET
class Hero:
    def __init__(self, speed=30):
        self.speed = speed
        self.life_points = 3
        self.width = 100
        self.height = 100
        self.image = pygame.image.load(os.path.join('assets/characters','hero.png'))
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (0.5 * WIDTH, 0.9 * HEIGHT)
        #przciski w zmiennych, aby możabyło zmieniać
        self.up = pygame.K_w
        self.down = pygame.K_s
        self.left = pygame.K_a
        self.right = pygame.K_d

    def hero_controls(self, keys_pressed):
        if keys_pressed[self.left]:
            if self.rect.x > 0.35 * WIDTH: #wartość ograniczenia ruchu w lewo
                self.rect.x -= self.speed
        if keys_pressed[self.right]:
            if self.rect.x < 0.58 * WIDTH: #wartość ograniczenia ruchu w prawo
                self.rect.x += self.speed
        
    def hero_draw(self):
        WIN.blit(self.image,(self.rect.x,self.rect.y))





