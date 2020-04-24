import pygame
import time
import random

#bludiste
SIRKA = 1000
VYSKA = 1000

BILA = (255, 255, 255)
MODRA = (0, 0, 255)
ZELENA = (0, 255, 0)
CERVENA = (255, 0, 0)
ORANZOVA = (255, 100, 10)
ZLUTA = (255, 255, 0)
LIMETKOVA = (180, 255, 100)
RUZOVA = (255, 100, 180)
FIALOVA = (240, 0, 255)

#pygame
pygame.init()
screen = pygame.display.set_mode((SIRKA, VYSKA), pygame.FULLSCREEN)
pygame.display.set_caption("Bludiste")
pygame.mixer.music.load("C:/Users/stank/Downloads/sound.mp3")
pygame.mixer.music.play()
font = pygame.font.Font(pygame.font.get_default_font(), 20)
text_surface = font.render("START", True, BILA)
screen.blit(text_surface, (5,10))
text_surface = font.render("FINISh", True, BILA)
screen.blit(text_surface, (900, 940))
clock = pygame.time.Clock()