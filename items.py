import pygame, os, random
from main import HEIGHT
#klasy
class Item(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 30
        self.height = 30
        self.velocity = 10
        self.position_x = random.randint(0,1600)
        self.position_y = 0
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets','square.webp')),(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.position_x, self.position_y)

    def item_move(self):
        self.rect.y += self.velocity
    def item_kill(self):
        if self.rect.y > HEIGHT:
            self.kill()


        
        
#eventy
            # if event.type == item_move:
            #     for element in item_list:
            #         element.item_move()
            # if event.type == item_spawn:
            #     item_list.append(Item())
#funkcje
def draw_sprites(WIN):
    all_sprites.update()
    all_sprites.draw(WIN)

#zmienne
all_sprites = pygame.sprite.Group()



    