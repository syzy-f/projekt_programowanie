import pygame, os, time, sys
from main_variables import WIN,WIDTH,HEIGHT


menu_state ="main"

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface=WIN):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
        
import pygame

pygame.init()

#create game window
WIN_WIDTH = WIDTH
WIN_HEIGHT = HEIGHT

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables


#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images


#create button instances


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  WIN.blit(img, (x, y))
#ZMIENNE
background_image = pygame.image.load(os.path.join ('assets/menu', "clicktoplay.png"))
background_resume_image = pygame.image.load(os.path.join ('assets/menu', "menu_background.png"))
play_button_img = pygame.image.load(os.path.join ('assets/menu', "play.png"))
options_button_img = pygame.image.load(os.path.join ('assets/menu', "options.png"))
easy_button_img = pygame.image.load(os.path.join ('assets/menu', "easy.png"))
medium_button_img = pygame.image.load(os.path.join ('assets/menu', "medium.png"))
hard_button_img = pygame.image.load(os.path.join ('assets/menu', "hard.png"))
levels_button_img = pygame.image.load(os.path.join ('assets/menu', "levels.png"))
resume_button_img = pygame.image.load(os.path.join ('assets/menu', "resume.png"))
quit_button_img = pygame.image.load(os.path.join ('assets/menu', "quit.png"))

start_button = Button(0.25*WIDTH,0.8*HEIGHT,play_button_img,0.1)
options_button = Button(0.75*WIDTH,0.8*HEIGHT,options_button_img,0.1)
levels_button = Button(0.5*WIDTH,0.2*HEIGHT,levels_button_img,0.1)
easy_button = Button(0.5*WIDTH,0.4*HEIGHT,easy_button_img,0.1)
medium_button = Button(0.5*WIDTH,0.6*HEIGHT,medium_button_img,0.1)
hard_button = Button(0.5*WIDTH,0.8*HEIGHT,hard_button_img,0.1)
resume_button = Button(0.25*WIDTH,0.8*HEIGHT,resume_button_img,0.1)
quit_button = Button(0.75*WIDTH,0.8*HEIGHT,quit_button_img,0.1)

#game loop
game_paused = False
menu_state = "main"
run = True
while run:


  #check if game is paused
    if game_paused == False:
        if menu_state == "main":
            WIN.blit(background_image,(0,0))
            if start_button.draw():
                menu_state = "game"
            if options_button.draw():
                menu_state = "options"
        if menu_state == "options":
            WIN.blit(background_resume_image,(0,0))
            levels_button.draw()
            if easy_button.draw():
                menu_state = "main"
            if medium_button.draw():
                menu_state = "main"
            if hard_button.draw():
                menu_state = "main"
    else:
        WIN.blit(background_resume_image,(0,0))
        resume_button.draw()
        quit_button.draw()

  #event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
    if event.type == pygame.QUIT:
      run = False

    pygame.display.update()

pygame.quit()