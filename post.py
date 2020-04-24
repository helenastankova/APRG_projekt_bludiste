import pygame
import time
import random

#bludiste
SIRKA = 500
VYSKA = 500

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
font = pygame.font.Font(pygame.font.get_default_font(), 12)
text_surface = font.render("start", True, BILA)
screen.blit(text_surface, (5,5))
text_surface = font.render("finish", True, BILA)
screen.blit(text_surface, (400, 430))
clock = pygame.time.Clock()