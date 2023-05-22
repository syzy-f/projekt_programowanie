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
CHARACTER_MODEL_WIDTH = 50
CHARACTER_MODEL_HEIGHT = 50
CHARACTER_MODEL = pygame.transform.scale(CHARACTER_MODEL_IMAGE,(CHARACTER_MODEL_WIDTH,CHARACTER_MODEL_HEIGHT))
#sterowanie wsad oraz prędkość
UP = pygame.K_w
DOWN = pygame.K_s
LEFT = pygame.K_a
RIGHT = pygame.K_d
VEL = 10

#główne okno gry
def draw_window(player):
    WIN.fill(WHITE)
    #wrzucenie modelu postaci do głównego oknaj
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
        keys_pressed=pygame.key.get_pressed()
        if keys_pressed[UP]:
            player.y-=VEL
        if keys_pressed[DOWN]:
            player.y+=VEL
        if keys_pressed[LEFT]:
            player.x-=VEL
        if keys_pressed[RIGHT]:
            player.x+=VEL
            
        draw_window(player)
    pygame.quit()

if __name__ == "__main__":
    main()