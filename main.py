import pygame, os, time, random
from items import *
from obstacles import Train, Fans
from main_variables import *
from characters import Hero
from menu import menu_stop, menu_end, menu_start


# WAŻNE
# większość z tego co jest poza główną pętlą warto wrzucić w funkcje/klasy i do osobnym plików, a potem je importować
# nie chiałbym jednak nikomu wchodzić w jego część zadania, więc śmiało zmieniajcie sobie to co jest do tej pory zrobione
# to tylko taki prototyp, aby zobrazować działanie pygame

pygame.init()
#tytuł okienka 
pygame.display.set_caption("Bimba Surfers")


current_time = 0

#główna pętla gry
def main():
    background_y = 0
    last_obstacle_spawn_time = pygame.time.get_ticks()


    #stworzenie obiektu klasy Hero - nasza postać
    player = Hero()

    #rozpoczęcie gry
    # starting = True
    running = True
    while running:
        menu_start()
        start = time.time()
        start_zatrzymania = 0
        stop_zatrzymania = 0
        run = True
        while run:
            for event in pygame.event.get():
                #kończenie programu poprzez X'a
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start_zatrzymania = time.time()
                        menu_stop()
                        stop_zatrzymania = time.time()
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_SPACE:
                #         run = False
            #spawnienie itemów i przeszkód
            lanes_with_obstacles = set()
            for obstacle in obstacles:
                if player.rect.colliderect(obstacle.rect):
                    run = False
                    #tutaj można zrobić jakieś GAME OVER albo zapisanie wyniku

            for lane in [0, 1, 2]:
                if lane not in lanes_with_obstacles:
                    if len(obstacles) == 0:
                        obstacle = Fans(lane)  #utworzenie przeszkody, gdy nie ma innych przeszkód
                        obstacles.add(obstacle)
                        all_sprites.add(obstacle)
                    else:
                        last_obstacle = max(obstacles, key=lambda o: o.rect.y)
                        if last_obstacle.rect.y > MIN_DISTANCE_BETWEEN_OBSTACLES:
                            if pygame.time.get_ticks() - last_obstacle_spawn_time > 800: #poniżej 800 jest dla koxów
                                obstacle_type = random.choice([Train, Fans,Hotdog,Coffee])
                                obstacle = obstacle_type(lane)  #wybór losowej przeszkody i wrzucenie jej do loswego lejnu
                                obstacles.add(obstacle)
                                all_sprites.add(obstacle)
                                last_obstacle_spawn_time = pygame.time.get_ticks()
                                
                    
            #funkcja pobierająca inputy z klawiatury odnośnie poruszania się
            player.hero_controls(pygame.key.get_pressed())
            #rysowanie tła
            background_y += VEL
            if background_y >= background.get_height():
                background_y = 0  #tło idzie w dół
            WIN.blit(background, (0, background_y - background.get_height()))  #tło
            WIN.blit(background, (0, background_y))
            player.hero_draw()
            
            for element in all_sprites:
                element.item_kill()
                element.item_collide(player.rect)
                element.item_move()
            all_sprites.draw(WIN)
            #odświeżanie ekranu
            pygame.display.flip()
            pygame.display.update()
            clock.tick(FPS)
            print(clock.get_fps())

        stop = time.time()
        menu_end(start, stop, start_zatrzymania, stop_zatrzymania)

if __name__ == "__main__":
    main()
