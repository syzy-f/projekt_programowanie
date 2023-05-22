import pygame, os, random
#klasy
class Item():
    def __init__(self):
        self.width = 30
        self.height = 30
        self.velocity = 10
        self.position_x = random.randint(0,1600)
        self.position_y = 0
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets','square.webp')),(self.width,self.height))
    def item_spawn(self):
        rect = pygame.Rect(self.position_x,self.position_y,self.width,self.height)
    def item_move(self):
        self.position_y += self.velocity
        
#eventy

#funkcje

#zmienne
item_list = [Item()]
def draw_item(item,WIN):
    WIN.blit(item.image,(item.position_x,item.position_y))
    