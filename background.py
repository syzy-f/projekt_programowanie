background = pygame.image.load('Assets',"background.png")  # Wczytanie obrazu tła




#żeby tło się elegancko przesuwało w dół, tworząc iluzję biegu

background_s = 0


background_s += OBSTACLE_SPEED  # Przesunięcie tła w dół używając zmiennej prędkości przeszkody
    if background_s >= background.get_height():
        background_s = 0  # Przewijanie tła, gdy osiągnie dolny kraniec

    screen.blit(background, (0, background_s - background.get_height()))  # Wyświetlanie tła
    screen.blit(background, (0, background_s))
    all_sprites.draw(screen)  # Wyświetlanie wszystkich obiektów na ekranie
