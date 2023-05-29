
class Hero:
    def __init__(self, x, y, speed=5):
        self.x = x
        self.y = y
        self.speed = speed
        self.life_points = 100

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

        if self.x < 0:
            self.x = 0
        elif self.x > WINDOW_WIDTH - HERO_SIZE:
            self.x = WINDOW_WIDTH - HERO_SIZE
        if self.y < 0:
            self.y = 0
        elif self.y > WINDOW_HEIGHT - HERO_SIZE:
            self.y = WINDOW_HEIGHT - HERO_SIZE

    def draw(self, surface):
        surface.blit(HERO_IMAGE, (self.x, self.y))

hero = Hero(100, 100, speed=5)

