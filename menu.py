import pygame, os, time, sys
from main_variables import WIN,WIDTH,HEIGHT
from characters import Hero

menu_state ="main"

class Button():
	def __init__(self, x, y, image, scale):
		self.width = image.get_width()
		self.height = image.get_height()
		self.scale = scale
		self.image = pygame.transform.scale(image, (int(self.width * self.scale), int(self.height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x-((self.width * self.scale)/2), y)
		self.clicked = False
	def draw(self, surface=WIN):
		action = False
		#pozycja myszki
		pos = pygame.mouse.get_pos()

		#sprawdzenie hoveru i kliknięcia
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#rysowanie buttona
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

def change_position(button,x,y):
    button.rect.topleft = ((WIDTH*x)-((button.width * button.scale)/2), HEIGHT *y)



#ZMIENNE
background_image = pygame.image.load(os.path.join ('assets/menu', "clicktoplay.png"))
background_resume_image = pygame.image.load(os.path.join ('assets/menu', "menu_background.png"))
background_lost_image = pygame.image.load(os.path.join ('assets/menu', "theend.png"))

play_button_img = pygame.image.load(os.path.join ('assets/menu', "play.png"))
options_button_img = pygame.image.load(os.path.join ('assets/menu', "options.png"))
easy_button_img = pygame.image.load(os.path.join ('assets/menu', "easy.png"))
medium_button_img = pygame.image.load(os.path.join ('assets/menu', "medium.png"))
hard_button_img = pygame.image.load(os.path.join ('assets/menu', "hard.png"))
levels_button_img = pygame.image.load(os.path.join ('assets/menu', "levels.png"))
resume_button_img = pygame.image.load(os.path.join ('assets/menu', "resume.png"))
quit_button_img = pygame.image.load(os.path.join ('assets/menu', "quit.png"))

start_button = Button(0.25*WIDTH,0.8*HEIGHT,play_button_img,0.1)
options_button = Button(0.5*WIDTH,0.8*HEIGHT,options_button_img,0.1)
levels_button = Button(0.5*WIDTH,0.4*HEIGHT,levels_button_img,0.1)
easy_button = Button(0.25*WIDTH,0.6*HEIGHT,easy_button_img,0.1)
medium_button = Button(0.5*WIDTH,0.6*HEIGHT,medium_button_img,0.1)
hard_button = Button(0.75*WIDTH,0.6*HEIGHT,hard_button_img,0.1)
resume_button = Button(0.25*WIDTH,0.6*HEIGHT,resume_button_img,0.1)
quit_button = Button(0.75*WIDTH,0.6*HEIGHT,quit_button_img,0.1)

