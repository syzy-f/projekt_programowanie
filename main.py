import pygame
import os
import sys
import time
import random
from items import Coffee, Hotdog
from obstacles import Train, Fans
from main_variables import *
from characters import Hero
from menu import *
from soundtrack import play_soundtrack

# WAŻNE
# większość z tego co jest poza główną pętlą warto wrzucić w funkcje/klasy i do osobnym plików, a potem je importować
# nie chiałbym jednak nikomu wchodzić w jego część zadania, więc śmiało zmieniajcie sobie to co jest do tej pory zrobione
# to tylko taki prototyp, aby zobrazować działanie pygame

pygame.init()
# Tytuł okienka
pygame.display.set_caption("Bimba Surfers")


current_time = 0
background_y = 0
last_obstacle_spawn_time = pygame.time.get_ticks()
czcionka = pygame.font.SysFont("arialblack", 210)
kolor_tekstu = (255, 255, 255)

# Główna pętla gry
main_loop = True
game_running = False
menu_state = "main"
player = Hero()
difficulty = "easy"
play_soundtrack() #soundtrack
while main_loop:
    #Menu
    if game_running == False: 
        
        if menu_state == "main":
            WIN.blit(background_image,(0,0))
            if start_button.draw():
                menu_state = "pause"
                game_running = True
                start = time.time()
                start_zatrzymania = 0
                stop_zatrzymania = 0
            if options_button.draw():
                menu_state = "options"
            #Zmiana połozenia przycisku
            change_position(quit_button,0.75,0.8)
            if quit_button.draw():
                pygame.quit()
        elif menu_state == "options":
            WIN.blit(background_resume_image,(0,0))
            levels_button.draw()
            if easy_button.draw():
                difficulty = "easy"

                menu_state = "main"
            if medium_button.draw():
                difficulty = "medium"
                menu_state = "main"
            if hard_button.draw():
                difficulty = "hard"
                menu_state = "main"
        elif menu_state == "pause":
            WIN.blit(background_resume_image,(0,0))
            change_position(quit_button,0.75,0.6)
            if resume_button.draw():
                game_running = True
            if quit_button.draw():
                pygame.quit()
        elif menu_state == "lost":
            WIN.blit(background_lost_image,(0,0))
            change_position(quit_button,0.75,0.6)
            czas_zatrzymania = stop_zatrzymania - start_zatrzymania
            czas_trwania = stop - start - czas_zatrzymania
            zaokraglony_czas_trawania = round(czas_trwania, 2)
            napis = czcionka.render(str(zaokraglony_czas_trawania), True, kolor_tekstu)
            if zaokraglony_czas_trawania < 10:
                WIN.blit(napis, (0.35*WIDTH,0.5*HEIGHT))
            else:
                WIN.blit(napis, (0.30*WIDTH,0.5*HEIGHT))
            if restart_button.draw():
                menu_state = "main"
                game_running = False
                player.lives = 3
            if quit_button.draw():
                pygame.quit()
    else:
        #Tło
        background_y += VEL
        if background_y >= background.get_height():
            # Tło idzie w dół
            background_y = 0
        WIN.blit(background, (0, background_y - background.get_height()))
        WIN.blit(background, (0, background_y))
        #Koniec tła
        
        #Postać
        player.hero_draw()
        player.update_animation()
        player.hero_controls(pygame.key.get_pressed())
        player.show_lives()
        #Koniec postaci
        
        #Itemy
        lanes_with_obstacles = set()

        for lane in [0, 1, 2]:
            if lane not in lanes_with_obstacles:
                if len(track_obstacles) == 0:
                    track_obstacle = Fans(lane)  #utworzenie przeszkody, gdy nie ma innych przeszkód
                    track_obstacles.add(track_obstacle)
                    lanes_with_obstacles.add(lane)
                else:
                    last_obstacle = max(track_obstacles, key=lambda o: o.rect.y)
                    if last_obstacle.rect.y > MIN_DISTANCE_BETWEEN_OBSTACLES:
                        if pygame.time.get_ticks() - last_obstacle_spawn_time > difficulty_level(difficulty)[1]: # Poniżej 800 jest dla koxów
                            # Wybór losowego toru
                            print(difficulty_level(difficulty)[1])
                            random_lane = random.choice([0, 1, 2])
                            if random_lane not in lanes_with_obstacles:
                                # Losowy wybór przeszkody/bonusu
                                random_number = random.random()  
                                if random_number < difficulty_level(difficulty)[0]:  # 80% szansy na pojawienie się przeszkody, można manipulować przy poziomie trudności
                                    track_obstacle_type = random.choice([Train, Fans])
                                else:  # 20% szansy na pojawienie się "coffee" lub "hotdog"
                                    track_obstacle_type = random.choice([Coffee, Hotdog])
                                track_obstacle = track_obstacle_type(random_lane)
                                # Dodanie wygenerowanego itemu do odpowiedniego toru
                                track_obstacles.add(track_obstacle)
                                lanes_with_obstacles.add(random_lane)
                                last_obstacle_spawn_time = pygame.time.get_ticks()
        track_obstacles.update()
        track_obstacles.draw(WIN)
        #Koniec itemów
        
        #Kolizcje
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
        #Koniec kolizji

        
        
        #Koniec gry
        if player.lives <= 0:
            game_running = False
            menu_state = "lost"
            #Zatrzymanie licznika
            stop = time.time()
            #Wyczyszczenie grupy spritów
            track_obstacles.empty()
        
        stop = time.time()
        czas_zatrzymania = stop_zatrzymania - start_zatrzymania
        czas_trwania = stop - start - czas_zatrzymania
        zaokraglony_czas_trawania = round(czas_trwania, 1)
        napis = czcionka.render(str(zaokraglony_czas_trawania), True, kolor_tekstu)
        if zaokraglony_czas_trawania < 10:
            WIN.blit(napis, (0.75*WIDTH,0.7*HEIGHT))
        else:
            WIN.blit(napis, (0.68*WIDTH,0.7*HEIGHT))
        #Odświeżanie
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)
        
            
    #eventy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_running = False
    
    pygame.display.update()