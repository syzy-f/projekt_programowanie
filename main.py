import pygame
import os
import time
import random
from items import Coffee, Hotdog
from obstacles import Train, Fans
from main_variables import *
from characters import Hero
from menu import menu_stop, menu_end, menu_start

# WAŻNE
# większość z tego co jest poza główną pętlą warto wrzucić w funkcje/klasy i do osobnym plików, a potem je importować
# nie chiałbym jednak nikomu wchodzić w jego część zadania, więc śmiało zmieniajcie sobie to co jest do tej pory zrobione
# to tylko taki prototyp, aby zobrazować działanie pygame

pygame.init()
# Tytuł okienka
pygame.display.set_caption("Bimba Surfers")


current_time = 0


# Główna pętla gry
def main():
    background_y = 0
    last_obstacle_spawn_time = pygame.time.get_ticks()

    # Stworzenie obiektu klasy Hero - nasza postać
    

    # Rozpoczęcie gry
    # starting = True
    running = True
    while running:
        player = Hero()
        menu_start()
        start = time.time()
        start_zatrzymania = 0
        stop_zatrzymania = 0
        run = True
        while run:

            for event in pygame.event.get():
                # Kończenie programu poprzez X'a
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start_zatrzymania = time.time()
                        menu_stop()
                        stop_zatrzymania = time.time()

            # Spawnienie bonusów i przeszkód
            lanes_with_obstacles = set()

            for lane in [0, 1, 2]:
                if lane not in lanes_with_obstacles:
                    if len(track_obstacles) == 0:
                        track_obstacle = Fans(lane)  # Utworzenie przeszkody, gdy nie ma innych przeszkód
                        track_obstacles.add(track_obstacle)
                    else:
                        last_obstacle = max(track_obstacles, key=lambda o: o.rect.y)
                        if last_obstacle.rect.y > MIN_DISTANCE_BETWEEN_OBSTACLES:
                            if pygame.time.get_ticks() - last_obstacle_spawn_time > 800: # Poniżej 800 jest dla koxów
                                # Losowy wybór przeszkody/bonusu
                                track_obstacle_type = random.choice([Train, Fans, Hotdog, Coffee])
                                track_obstacle = track_obstacle_type(lane)
                                # Wybór losowej przeszkody i wrzucenie jej do losowego toru
                                track_obstacles.add(track_obstacle)
                                last_obstacle_spawn_time = pygame.time.get_ticks()
                                
            # Funkcja pobierająca inputy z klawiatury odnośnie poruszania się
            player.hero_controls(pygame.key.get_pressed())

            # Jeżeli gracz starci wszsytkie życia - zakończ grę
            if player.lives < 1:
                run = False
            else:
                print(player.lives)

            # Rysowanie tła
            background_y += VEL
            if background_y >= background.get_height():
                # Tło idzie w dół
                background_y = 0

            # Tło
            WIN.blit(background, (0, background_y - background.get_height()))
            WIN.blit(background, (0, background_y))
            player.hero_draw()
            player.update_animation()

            # Aktualizacja połoażenia wszystkich obiektów
            track_obstacles.update()
            track_obstacles.draw(WIN)

            # Sprawdzenie kolizji z obiektami na torach
            for element in track_obstacles:
                if element.__class__.__name__ == "Hotdog":
                    element.hotdog_collide(player)
                if element.__class__.__name__ == "Coffee":
                    element.coffee_collide(player)
                if element.__class__.__name__ == "Fans":
                    element.fans_collide(player) 
                if element.__class__.__name__ == "Train":
                    element.train_collide(player)
                element.item_collide(player)
            # Rysuj życia gracza po narysowaniu wszystkiego (zawsze na wierzchu)
            player.show_lives()

            # Odświeżanie ekranu
            pygame.display.flip()
            pygame.display.update()
            clock.tick(FPS)

        stop = time.time()
        menu_end(start, stop, start_zatrzymania, stop_zatrzymania)


if __name__ == "__main__":
    main()
