
HERO_SIZE = 128
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (244, 220, 181)

HERO_IMAGE = pygame.image.load(os.path.join('Assets', 'hero.png'))
HERO_IMAGE = pygame.transform.scale(HERO_IMAGE, (HERO_SIZE, HERO_SIZE))

rectangle_surface = pygame.Surface((HERO_SIZE, HERO_SIZE), pygame.SRCALPHA)
pygame.draw.rect(rectangle_surface, (0, 0, 0, 100), (0, 0, HERO_SIZE, HERO_SIZE))

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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    delta_x = 0
    delta_y = 0
    if keys[pygame.K_LEFT]:
        delta_x -= hero.speed
    if keys[pygame.K_RIGHT]:
        delta_x += hero.speed
    if keys[pygame.K_UP]:
        delta_y -= hero.speed
    if keys[pygame.K_DOWN]:
        delta_y += hero.speed
    if keys[pygame.K_ESCAPE]:
        running = False

    hero.move(delta_x, delta_y)
    window.fill(BACKGROUND_COLOR)
    hero.draw(window)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

