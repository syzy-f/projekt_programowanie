import pygame, os
WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#tytuł okienka 
pygame.display.set_caption("Bimba Surfers")

WHITE = (255,255,255)

#liczba fpsów
FPS = 60
#import modelu postaci
CHARACTER_MODEL_IMAGE = pygame.image.load(os.path.join('assets','mario.png'))
#zmiana wielkości modelu postaci
CHARACTER_MODEL = pygame.transform.scale(CHARACTER_MODEL_IMAGE,(50,50))

#główne okno gry
def draw_window():
    WIN.fill(WHITE)
    #wrzucenie modelu postaci do głównego oknaj
    WIN.blit(CHARACTER_MODEL,(0.5*WIDTH,0.5*HEIGHT))
    pygame.display.update()
    
#główna pętla gry
def main():
    
    clock = pygame.time.Clock()
    run = True
    while run:
        #ogranicznik fpsów
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()