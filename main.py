import pygame, os, time
from controls import controls
from items import *
# WAŻNE
# większość z tego co jest poza główną pętlą warto wrzucić w funkcje/klasy i do osobnym plików, a potem je importować
# nie chiałbym jednak nikomu wchodzić w jego część zadania, więc śmiało zmieniajcie sobie to co jest do tej pory zrobione
# to tylko taki prototyp, aby zobrazować działanie pygame

pygame.init() 
#stałe
SCREEN_WIDTH = 1600  #WAŻNE
SCREEN_HEIGHT = 900  #WAŻNE
FPS = 60 
OBSTACLE_SPEED = 20  # Prędkość poruszania się przeszkód
LANE_WIDTH = (SCREEN_WIDTH - 4 * 390) // 3  # Szerokość toru
TOR_OFFSET = (SCREEN_WIDTH - (3 * LANE_WIDTH + 2 * 105)) // 2  #żeby tramwaje nie zjeżdżały
MIN_DISTANCE_BETWEEN_OBSTACLES = 400  #minimalna odległość między przeszkodami, edycja wpływa na poziom trudności gry!!!!!!!

WHITE = (255, 255, 255)  # Kolor biały w formacie RGB

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#tytuł okienka 
pygame.display.set_caption("Bimba Surfers")
#kolor okienka
WHITE = (255,255,255)


# to można do postaci przenieść
#import modelu postaci
CHARACTER_MODEL_IMAGE = pygame.image.load(os.path.join('assets','mario.png'))
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
item_spawn = pygame.USEREVENT
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
            #even spawnowania itemów
            if event.type == item_spawn:
                X = Coffee()
                all_sprites.add(X)
        #sterowanie funkcjonalność
        controls(pygame.key.get_pressed(),player)
        draw_window(player)
        for element in all_sprites:
            draw_sprites(WIN)
            element.item_kill()
            element.item_collide(player)
            element.item_move()
        # Update
        refresh()
    pygame.quit()

if __name__ == "__main__":
    main()
