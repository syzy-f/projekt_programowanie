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
    #ruch itemów
    def item_move(self):
        self.rect.y += self.velocity
    #znikanie itemów po wyleceniu za mape
    def item_kill(self):
        if self.rect.y > HEIGHT:
            self.kill()
    #znikanie itemów po kolizji z postacią, do dodania jeszcze dźwięk
    def item_collide(self,player):
        if pygame.Rect.colliderect(player,self.rect) == True:
            self.kill()


            
class Hotdog(Item):
    def __init__(self,lane):
        #nadpisanie niektórych właściwości na potrzeby klasy hotdog
        self.lane = lane
        self.scale = 0.05
        self.width = self.scale*WIDTH
        self.height = self.scale*HEIGHT
        self.image = pygame.image.load(os.path.join('assets/items','hotdog.png'))
        super().__init__()

        
class Coffee(Item):
    #podstawowe właściwości itemów
    def __init__(self, lane):
        #nadpisanie niektórych właściwości na potrzeby klasy coffee
        self.lane = lane
        self.width = 0.05*WIDTH
        self.height = 0.07*HEIGHT
        self.image = pygame.image.load(os.path.join('assets/items','caffee.png'))
        super().__init__()



        
        
#eventy
            # if event.type == item_move:
            #     for element in item_list:
            #         element.item_move()
            # if event.type == item_spawn:
            #     item_list.append(Item())
            
#funkcja wrzucająca na ekran wszystkiei itemy
def draw_sprites(WIN):
    all_sprites.update()
    all_sprites.draw(WIN)

#zmienne




    