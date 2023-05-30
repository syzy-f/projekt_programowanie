import pygame, time
from menu import menu_start, menu_end, menu_stop
from main import main

pygame.init()
pygame.display.set_caption("Bimba Surfers")


menu_start()
start = time.time()
main()
stop = time.time()
menu_end(start, stop)

pygame.quit()