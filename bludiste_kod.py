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

#pocatecni souradnice
startX = 20
startY = 20

x = startX
y = startY

sit = []
navstivena = []
zasobnik = []
reseni = {}


#vytvari sit pro bludiste
def sit_pro_bludiste(x, y, z, screen,pocet_bunek_v_radku, pocet_bunek_v_sloupci):
    for a in range(1, pocet_bunek_v_sloupci+ 1):
        x = startX
        for b in range(1, pocet_bunek_v_radku + 1):
            pygame.draw.line(screen, BILA, [x, y], [x + z, y], 2)
            pygame.draw.line(screen, BILA, [x + z, y], [x + z, y + z], 2)
            pygame.draw.line(screen, BILA, [x + z, y + z], [x, y + z], 2)
            pygame.draw.line(screen, BILA, [x, y + z], [x, y], 2)
            sit.append((x, y))
            x = x + z
        y = y + z

#definice potrebnych bunek
def bunka(x, y, z, screen):
    pygame.draw.rect(screen, CERVENA, (x + 1, y + 1, z - 2, z - 2), 0)
    pygame.display.update()

def bunka_2(x, y,z, screen, barva):
    pygame.draw.rect(screen, barva, (x + 1, y + 1, z - 2, z - 2), 0)
    pygame.display.update()

def vysledna_bunka_doprava(x, y, screen):
    image = pygame.image.load("pacicka.png")
    image = pygame.transform.scale(image, (12, 12))
    image = pygame.transform.rotate(image, -90)
    screen.blit(image, (x, y + 5))
    pygame.display.update()

def vysledna_bunka_dolu(x, y, screen):
    image = pygame.image.load("pacicka.png")
    image = pygame.transform.scale(image, (12, 12))
    image = pygame.transform.rotate(image, 180)
    screen.blit(image, (x + 5, y))
    pygame.display.update()

def vysledna_bunka_doleva(x, y, screen):
    image = pygame.image.load("pacicka.png")
    image = pygame.transform.scale(image, (12, 12))
    image = pygame.transform.rotate(image, 90)
    screen.blit(image, (x + 3, y + 5))
    pygame.display.update()

def vysledna_bunka_nahoru(x, y, screen):
    image = pygame.image.load("pacicka.png")
    image = pygame.transform.scale(image, (12, 12))
    screen.blit(image, (x + 5, y + 3))
    pygame.display.update()

#definice simulace smazani steny mezi dvema bunkami
def nahoru(x, y, z, screen, barva):
    pygame.draw.rect(screen, barva, (x + 1, y - z + 1, z - 1, (2 * z) - 1), 0)
    pygame.display.update()

def dolu(x, y,z, screen, barva):
    pygame.draw.rect(screen, barva, (x + 1, y + 1, z - 1, (2 * z) - 1), 0)
    pygame.display.update()

def doleva(x, y, z, screen, barva):
    pygame.draw.rect(screen, barva, (x - z + 1, y + 1, (2 * z) - 1, z - 1), 0)
    pygame.display.update()

def doprava(x, y,z,  screen, barva):
    pygame.draw.rect(screen, barva, (x + 1, y + 1, (2 * z) - 1, z - 1), 0)
    pygame.display.update()

#vykreslovani bludiste, tvoreni chodeb
def bludiste(x, y, z, screen, barva):
    bunka(x, y,z, screen)
    navstivena.append((x, y))
    zasobnik.append((x, y))
    while len(zasobnik) > 0:
        time.sleep(.0001)
        nova_bunka = []

        if (x, y - z) not in navstivena and (x, y - z) in sit:
            nova_bunka.append("nahoru")
        if (x, y + z) not in navstivena and (x, y + z) in sit:
            nova_bunka.append("dolu")
        if (x - z, y) not in navstivena and (x - z, y) in sit:
            nova_bunka.append("doleva")
        if (x + z, y) not in navstivena and (x + z, y) in sit:
            nova_bunka.append("doprava")

        if len(nova_bunka) > 0:
            vybrana_bunka = (random.choice(nova_bunka))

            if vybrana_bunka == "doprava":
                doprava(x, y,z, screen, barva)
                reseni[(x + z, y)] = x, y
                x = x + z
                navstivena.append((x, y))
                zasobnik.append((x, y))

            elif vybrana_bunka == "doleva":
                doleva(x, y,z, screen, barva)
                reseni[(x - z, y)] = x, y
                x = x - z
                navstivena.append((x, y))
                zasobnik.append((x, y))

            elif vybrana_bunka == "nahoru":
                nahoru(x, y,z, screen, barva)
                reseni[(x, y - z)] = x, y
                y = y - z
                navstivena.append((x, y))
                zasobnik.append((x, y))

            elif vybrana_bunka == "dolu":
                dolu(x, y,z, screen, barva)
                reseni[(x, y + z)] = x, y
                y = y + z
                navstivena.append((x, y))
                zasobnik.append((x, y))
        else:
            x, y = zasobnik.pop()
            bunka(x, y,z, screen)
            time.sleep(.05)
            bunka_2(x, y,z, screen, barva)

#modeluje cestu zpet a nataci pacicku do spravneho smeru
def cesta_zpet(x, y, z, screen):
    vysledna_bunka_doleva(x, y, screen)
    y1 = float("inf")
    x1 = 0
    while (x, y) != (startX, startY):
        x, y = reseni[x, y]
        if y1 == y:
            if x1 < x:
                vysledna_bunka_doprava(x, y, screen)
            else:
                vysledna_bunka_doleva(x, y, screen)
        else:
            if y1 < y:
                vysledna_bunka_dolu(x, y, screen)
            else:
                vysledna_bunka_nahoru(x, y, screen)
        time.sleep(.1)
        y1 = y
        x1 = x

def main():
    # inicializace pygamu
    pygame.init()

    z = 20
    x, y = startX, startY

    # uzivatel si vybira barvu bludiste
    print("MODRA = 1, ZELENA = 2, ORANZOVA = 3, ZLUTA = 4, FIALOVA = 5")
    cislo = int(input("Zadej cislo barvy bludiste:"))
    if cislo == 1:
        barva = MODRA
    if cislo == 2:
        barva = ZELENA
    if cislo == 3:
        barva = ORANZOVA
    if cislo == 4:
        barva = ZLUTA
    if cislo == 5:
        barva = FIALOVA

    # libovolne zadani velikosti bludiste uzivatelem
    pocet_bunek_v_radku = int(input("Zadej pocet bunek v radku:"))
    pocet_bunek_v_sloupci = int(input("Zadej pocet bunek v sloupci:"))
    if (pocet_bunek_v_radku or pocet_bunek_v_sloupci) > 48:
        input("Pozadovanane rozmery jsou moc velké!")

    screen = pygame.display.set_mode((SIRKA, VYSKA), pygame.FULLSCREEN)
    pygame.display.set_caption("Bludiste")
    pygame.mixer.music.load("znelka.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(2)

    font = pygame.font.Font(pygame.font.get_default_font(), 15)
    #text_surface = font.render("FINISH", True, BILA)
    #screen.blit(text_surface, (5, 5))
    #image = pygame.image.load("start.png")
    #screen.blit(image, (930, 900))
    image2 = pygame.image.load("cil.png")
    image2 = pygame.transform.scale(image2, (32, 32))
    screen.blit(image2, (-3, -7))
    clock = pygame.time.Clock()
    sit_pro_bludiste(startX, startY, z, screen,pocet_bunek_v_radku,pocet_bunek_v_sloupci)
    bludiste(x, y,z, screen, barva)
    cesta_zpet(pocet_bunek_v_radku * z, pocet_bunek_v_sloupci * z, z, screen)

    running = True
    while running:
        pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ =="__main__":
    main()



