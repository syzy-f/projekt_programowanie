import pygame, os, time
from controls import controls
from items import *
# WAŻNE
# większość z tego co jest poza główną pętlą warto wrzucić w funkcje/klasy i do osobnym plików, a potem je importować
# nie chiałbym jednak nikomu wchodzić w jego część zadania, więc śmiało zmieniajcie sobie to co jest do tej pory zrobione
# to tylko taki prototyp, aby zobrazować działanie pygame

# to można do mapy przenieść
#szerokość i wysokość okienka
WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#tytuł okienka 
pygame.display.set_caption("Bimba Surfers")
#kolor okienka
WHITE = (255,255,255)

#liczba fpsów
FPS = 60

# to można do postaci przenieść
#import modelu postaci
CHARACTER_MODEL_IMAGE = pygame.image.load(os.path.join('assets','juki.webp'))
#zmiana wielkości modelu postaci
CHARACTER_MODEL_WIDTH = 200
CHARACTER_MODEL_HEIGHT = 200
CHARACTER_MODEL = pygame.transform.scale(CHARACTER_MODEL_IMAGE,(CHARACTER_MODEL_WIDTH,CHARACTER_MODEL_HEIGHT))




#główne okno gry
def draw_window(player):
    WIN.fill(WHITE)
    #wrzucenie modelu postaci do głównego okna
    WIN.blit(CHARACTER_MODEL,(player.x,player.y))
        
#event z itemami
item_move = pygame.USEREVENT + 1
pygame.time.set_timer(item_move,20)
item_spawn = pygame.USEREVENT + 2
pygame.time.set_timer(item_spawn,1000)

def refresh():
    pygame.display.update()
current_time = 0
#główna pętla gry
def main():
    player = pygame.Rect(0.5*WIDTH,0.5*HEIGHT,CHARACTER_MODEL_HEIGHT,CHARACTER_MODEL_WIDTH)
    clock = pygame.time.Clock()
    run = True
    while run:
        #ogranicznik fpsów
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == item_move:
                for element in all_sprites:
                    element.item_move()
            if event.type == item_spawn:
                all_sprites.add(Car())
        #sterowanie funkcjonalność
        controls(pygame.key.get_pressed(),player)
        draw_window(player)
        for element in all_sprites:
            draw_sprites(WIN)
            element.item_kill()
        # Update
        refresh()
    pygame.quit()

if __name__ == "__main__":
    main()