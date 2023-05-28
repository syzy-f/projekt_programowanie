#klasy przeszkód
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, lane):
        super().__init__()
        self.image = obstacle_image  # Załadowanie obrazu przeszkody
        self.rect = self.image.get_rect()  # Utworzenie prostokątnego obszaru ograniczającego przeszkodę
        self.lane = lane  
        self.rect.centerx = TOR_OFFSET + LANE_WIDTH // 2 + self.lane * (LANE_WIDTH + 97)  # Ustalenie pozycji poziomej przeszkody, to "97" to dodałem, żeby dobrze ulokować obiekty na tle względem rozdzielczości 1600x900, możliwe że potem trzeba będzie to zmienić
        self.rect.y = -random.randrange(200, 600)  # Ustalenie początkowej pozycji pionowej przeszkody

    def update(self):
        self.rect.y += OBSTACLE_SPEED  # Przesunięcie przeszkody w dół

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Usunięcie przeszkody, gdy opuści obszar ekranu
            
#dodałem też drugą przeszkodę dla urozmaicenia gry, będą się różniły wymiarami. Przeszkoda 1 przy rozdzielczości 1600x900 ma wymiary 300x100, a przeszkoda 2 100x100. 
#adnotacja dla mnie - ograniczyć liczbę kibiców Lecha Poznań, bo to gra o tramwajach

class Obstacle2(pygame.sprite.Sprite): 
    def __init__(self, lane):
        super().__init__()
        self.image = obstacle2_image  
        self.rect = self.image.get_rect()  
        self.lane = lane  
        self.rect.centerx = TOR_OFFSET + LANE_WIDTH // 2 + self.lane * (LANE_WIDTH + 97)  
        self.rect.y = -random.randrange(200, 600)  

    def update(self):
        self.rect.y += OBSTACLE_SPEED  

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  
