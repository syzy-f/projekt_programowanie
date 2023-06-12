import pygame, os, time, sys

class Przyciski():
    def __init__(self, x, y, obrazek, skala):
        szerokosc = obrazek.get_width()
        wysokosc = obrazek.get_height()
        self.image = pygame.transform.scale(obrazek, (int(szerokosc * skala), int(wysokosc * skala)))
        self.prostokat = self.image.get_rect()
        self.prostokat.topleft = (x, y)
        self.klikniete = False
    
    def narysuj(self, powierzchnia):
        action = False
        pozycja_myszki = pygame.mouse.get_pos()
        if self.prostokat.collidepoint(pozycja_myszki):
            if pygame.mouse.get_pressed()[0] == 1 and not self.klikniete:
                self.klikniete = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.klikniete = False
        powierzchnia.blit(self.image, self.prostokat.topleft)
        return action

def wyswietlanie_tekstu(tekst, czcionka, kolor_tekstu, x, y):
    wyswietlacz = pygame.display.set_mode((1600, 900))
    napis = czcionka.render(tekst, True, kolor_tekstu)
    wyswietlacz.blit(napis, (x, y))

def menu_start():
    wyswietlacz = pygame.display.set_mode((1600, 900))
    clicktoplay = pygame.image.load(os.path.join ('assets/menu', "clicktoplay.png"))
    play_obrazek = pygame.image.load(os.path.join ('assets/menu', "play.png"))
    play_przycisk = Przyciski(660, 650, play_obrazek, 0.19)
    running = True
    while running:
        wyswietlacz.blit(clicktoplay, (0,0))
        if play_przycisk.narysuj(wyswietlacz):
            return False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        pygame.display.update()

def menu_stop():
    wyswietlacz = pygame.display.set_mode((1600, 900))

    background_menu = pygame.image.load(os.path.join ('assets/menu', "menu_background.png"))

    resume_obrazek = pygame.image.load(os.path.join ('assets/menu', "resume.png"))
    quit_obrazek = pygame.image.load(os.path.join ('assets/menu', "quit.png"))

    quit_przycisk = Przyciski(600, 600, quit_obrazek, 0.22)
    resume_przycisk = Przyciski(600, 350, resume_obrazek, 0.22)
    
    zastopowac_gre = True
    while zastopowac_gre:
        wyswietlacz.blit(background_menu, (0,0))
        if resume_przycisk.narysuj(wyswietlacz):
            zastopowac_gre = False
        elif quit_przycisk.narysuj(wyswietlacz):
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        pygame.display.update()


def menu_end(start, stop, start_zatrzymania, stop_zatrzymania):
    wyswietlacz = pygame.display.set_mode((1600, 900))

    theend = pygame.image.load(os.path.join ('assets/menu', "theend.png"))
    quit_obrazek = pygame.image.load(os.path.join ('assets/menu', "quit.png"))
    restart_obrazek = pygame.image.load(os.path.join ('assets/menu', "restart.png"))

    quit_przycisk = Przyciski(1200, 500, quit_obrazek, 0.15)
    restart_przycisk = Przyciski(150, 500, restart_obrazek, 0.15)

    running = True
    while running:
        wyswietlacz.blit(theend, (0,0))
        czas_zatrzymania = stop_zatrzymania - start_zatrzymania
        czas_trwania = stop - start - czas_zatrzymania
        zaokraglony_czas_trawania = round(czas_trwania, 2)
        napis = czcionka.render(str(zaokraglony_czas_trawania), True, kolor_tekstu)
        wyswietlacz.blit(napis, (510, 400))
        if restart_przycisk.narysuj(wyswietlacz):
            return False
        elif quit_przycisk.narysuj(wyswietlacz):
            sys.exit()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        pygame.display.update()

pygame.init()

pygame.display.set_caption("Menu")
czcionka = pygame.font.SysFont("arialblack", 250)
kolor_tekstu = (255, 255, 255)
