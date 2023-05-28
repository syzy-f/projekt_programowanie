#klasa postaci do zrobienia
import pygame
import pygame
import os   #operating system

pygame.init()       #inicjalizuje pygame

#okno gry - ustawienia
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("BIBMA SURFERS")


#kolor okna
WHITE=(255,255,255)
BLACK=(0, 0 , 0)    #code for black - none of red, none of blue, none of green

#częstotliwość odświeżania
FPS = 60       #60 time per second, żeby na każdym kompie tak samo szybko się pojawiało
#prędkość
VEL = 8

#obrazek bohatera
HERO_WIDTH = 55
HERO_HEIGHT = 40
HERO_IMAGE= pygame.image.load(os.path.join('Assets','hero1.png')) #os po to żeby auomatycznie działało na windowsie czy macu
HERO_IMAGE = pygame.transform.rotate(pygame.transform.scale(HERO_IMAGE,(HERO_WIDTH, HERO_HEIGHT)), 90)
                                    

def draw_window(hero):
    window.fill(WHITE)
    pygame.draw.rect(window, BLACK (hero.x, hero.y, HERO_WIDTH, HERO_HEIGHT))
    window.blit(HERO_IMAGE,(hero.x, hero.y))        #draw the surface on the screen
    pygame.display.update()
    

def draw_rectangle(x, y, rectangle_width, rectangle_height):
    rectangle_surface = pygame.Surface((rectangle_width, rectangle_height), pygame.SRCALPHA)  # Utworzenie powierzchni z przezroczystością
    pygame.draw.rect(rectangle_surface, (0, 0, 0, 0), (0, 0, rectangle_width, rectangle_height))  # Rysowanie przezroczystego prostokąta
    window.blit(rectangle_surface, (x, y))  # Wyświetlanie powierzchni na oknie gry


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
            
            
def main():
    hero = Hero(100,300)                                  
    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)     #stała szybkość na różnych komputerach
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
        keys_pressed = pygame.key.get_pressed()
        hero.move(keys_pressed)
        draw_window(hero)

    pygame.QUIT()

#if __name__=="__main__":
#    main()
