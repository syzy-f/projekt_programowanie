import pygame, os
from controls import controls
WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#tytuł okienka 
pygame.display.set_caption("Bimba Surfers")

WHITE = (255,255,255)

#liczba fpsów
FPS = 60
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
    
    pygame.display.update()
    
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
        #sterowanie funkcjonalność
        controls(pygame.key.get_pressed(),player)

            
        draw_window(player)
    pygame.quit()

if __name__ == "__main__":
    main()