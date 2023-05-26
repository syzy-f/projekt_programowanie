#klasa postaci do zrobienia
import pygame
import pygame
import os   #operating system

pygame.init()       #inicjalizuje pygame

#okno gry - ustawienia
width, height = 900, 500
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Character is coming!")


#kolor okna
white=(255,255,255)
black=(0, 0 , 0)    #code for black - none of red, none of blue, none of green

#częstotliwość odświeżania
FPS = 60       #60 time per second, żeby na każdym kompie tak samo szybko się pojawiało
#prędkość
VEL = 8

#obrazek bohatera
MONSTER_WIDTH, MONSTER_HEIGHT = 55, 40
CUTE_MONSTER_IMAGE= pygame.image.load(os.path.join('Assets','hero1.png')
CUTE_MONSTER = pygame.transform.rotate(pygame.transfom.scale(CUTE_MONSTER_IMAGE,(MONSTER_WIDTH, MONSTER_HEIGHT)), 90)
                                    

def draw_window():
    window.fill(white)
    pygame.draw.rect(window, black (monster.x, monster.y, MONSTER.WIDTH, MONSTER.HEIGHT))
    window.blit(CUTE_MONSTER_IMAGE,(monster.x, monster.y))        #draw the surface on the screen
    pygame.display.update()


class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.life_points = 100
    def move(self,keys_pressed):
        
        if keys_pressed[pygame.K_a] and self.x - VEL >0:    #LEFT KEY, jak jest 0,0 to będzie poza ekranem
            self.x -= VEL
        if keys_pressed[pygame.K_d] and self.x + MONSTER_WIDTH + VEL < width:    #RIGHT KEY
            self.x += VEL
        if keys_pressed[pygame.K_w] and self.y - VEL > 0:    #UP KEY
            self.y -= VEL
        if keys_pressed[pygame.K_s] and self.y + MONSTER_HEIGHT + VEL < height:    #DOWN KEY
            self.y += VEL




MONSTER = Hero(x,y)



def main():
    monster = Hero(100,300)                                  
    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)     #stała szybkość na różnych komputerach
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
        keys.pressed = pygame.key.get_pressed()
        MONSTER.move(keys_pressed)

    draw.window(monster)
    


    pygame.quit()

#if _name_=="__main__":
#    main()
