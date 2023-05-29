import pygame, os, random
from main_variables import *
from items import Item


            
class Train(Item):
    def __init__(self, lane):
        #nadpisanie niektórych właściwości na potrzeby klasy train
        self.lane = lane
        self.width = 0.08*WIDTH
        self.height = 0.6*HEIGHT
        self.image = pygame.image.load(os.path.join('assets/obstacles','train.png'))
        super().__init__()

        
class Fans(Item):
    #podstawowe właściwości itemów
    def __init__(self, lane):
        #nadpisanie niektórych właściwości na potrzeby klasy fans
        self.lane = lane
        self.width = 0.10*WIDTH
        self.height = 0.10*HEIGHT
        self.image = pygame.image.load(os.path.join('assets/obstacles','fans.png'))
        super().__init__()



        
        
#eventy
            # if event.type == item_move:
            #     for element in item_list:
            #         element.item_move()
            # if event.type == item_spawn:
            #     item_list.append(Item())
            




    