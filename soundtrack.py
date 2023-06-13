import pygame
import os

def play_soundtrack():
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join('assets/music',"soundtrack.mp3"))
    pygame.mixer.music.set_volume(0.5)  #głośność, nie wiem czy potrzebna w sumie
    pygame.mixer.music.play(-1)  # pętla
