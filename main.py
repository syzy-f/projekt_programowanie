import pygame, os, time
from controls import controls
from items import *
from obstacles import *
# WAŻNE
# większość z tego co jest poza główną pętlą warto wrzucić w funkcje/klasy i do osobnym plików, a potem je importować
# nie chiałbym jednak nikomu wchodzić w jego część zadania, więc śmiało zmieniajcie sobie to co jest do tej pory zrobione
# to tylko taki prototyp, aby zobrazować działanie pygame

pygame.init() 
#stałe
SCREEN_WIDTH = 1600  #WAŻNE
SCREEN_HEIGHT = 900  #WAŻNE
FPS = 60 
OBSTACLE_SPEED = 20  # Prędkość poruszania się przeszkód, edycja wpływa na poziom trudności gry!!!!!!!
LANE_WIDTH = (SCREEN_WIDTH - 4 * 390) // 3  # Szerokość toru
TOR_OFFSET = (SCREEN_WIDTH - (3 * LANE_WIDTH + 2 * 105)) // 2  #żeby tramwaje nie zjeżdżały
MIN_DISTANCE_BETWEEN_OBSTACLES = 400  #minimalna odległość między przeszkodami, edycja wpływa na poziom trudności gry!!!!!!!

WIN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 
pygame.display.set_caption("Bimba Surfers")
WHITE = (255,255,255)

clock = pygame.time.Clock()  # Utworzenie obiektu Clock - używany do kontrolowania prędkości odświeżania ekranu

#wczytanie obrazów (brakuje postaci 50x50, ale oczywiście może mieć też inne wymiary, tylko trzeba je zmienić poniżej)
background = pygame.image.load('Assets', "background.png")  #tło
obstacle_image = pygame.image.load('Assets', "obstacle.png")  #tramwaje
obstacle2_image = pygame.image.load('Assets', "obstacle2.png")  #kibole

#skalowanie
player_images = [pygame.transform.scale(image, (50, 50)) for image in player_images]
obstacle_image = pygame.transform.scale(obstacle_image, (100, 300))  
obstacle2_image = pygame.transform.scale(obstacle2_image, (100, 100)) 

#ja jestem Sprite a ty jesteś pragnienie
all_sprites = pygame.sprite.Group() 
obstacles = pygame.sprite.Group()  

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

 background_s = 0

last_obstacle_spawn_time = pygame.time.get_ticks()

while running:
#tu trzeba dodać sterowanie!!!!!!!!!!!!!
    lanes_with_obstacles = set()
    for obstacle in obstacles:
        lanes_with_obstacles.add(obstacle.lane)

    for lane in [0, 1, 2]:
        if lane not in lanes_with_obstacles:
            if len(obstacles) == 0:
                obstacle = Obstacle(lane)  #utworzenie nowej przeszkody, gdy nie ma innych
                obstacles.add(obstacle)
                all_sprites.add(obstacle)
            else:
                last_obstacle = max(obstacles, key=lambda o: o.rect.y)
                if last_obstacle.rect.y > MIN_DISTANCE_BETWEEN_OBSTACLES:
                    if pygame.time.get_ticks() - last_obstacle_spawn_time > 750: #zmiana wpłynie na poziom trudności gry!!!!!!!!! 
                        obstacle_type = random.choice([Obstacle, Obstacle2])
                        obstacle = obstacle_type(lane)  # Wybór losowej przeszkody i ustawienie jej w torze
                        obstacles.add(obstacle)
                        all_sprites.add(obstacle)
                        last_obstacle_spawn_time = pygame.time.get_ticks()

    background_s += OBSTACLE_SPEED  #przesunięcie tła w dół
    if background_s >= background.get_height():
        background_s = 0  #przewijanie tła, gdy osiągnie dolny kraniec

    screen.blit(background, (0, background_s - background.get_height()))  #wyświetlanie tła
    screen.blit(background, (0, background_s))
    all_sprites.draw(screen)  # Wyświetlanie wszystkich obiektów na ekranie

    pygame.display.flip()  #istotne
    clock.tick(FPS)  

pygame.quit() 
