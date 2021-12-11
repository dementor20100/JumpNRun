import pygame
import sys

from Objekte.Spieler import Spieler
from Objekte.Kugel import Kugel
from Objekte.Zombie import Zombie
from Objekte.Util import Util
 
pygame.init()

hintergrund = pygame.image.load("Grafiken/hintergrund.png")
screen = pygame.display.set_mode([1200,595])
clock = pygame.time.Clock()

pygame.display.set_caption("Pygame Tutorial")
 
siegSound = pygame.mixer.Sound("Sounds/robosieg.wav")
verlorenSound = pygame.mixer.Sound("Sounds/robotod.wav")
siegBild = pygame.image.load("Grafiken/sieg.png")
verlorenBild = pygame.image.load("Grafiken/verloren.png")

def zeichnen():
    screen.blit(hintergrund, (0,0))
    for k in kugeln:
        k.zeichnen()
    spieler.zeichnen()
    zombie.zeichnen()
    zombie.herzen()
    if gewonnen:
        screen.blit(siegBild,(0,0))
    elif verloren:
        screen.blit(verlorenBild,(0,0))
    pygame.display.update()
 
def kugelHandler():
    global kugeln
    for k in kugeln:
        if k.x >= 0 and k.x <= 1200:
            k.bewegen()
        else:
            kugeln.remove(k)
 
def kollision():
    global kugeln, verloren, gewonnen, go
    zombieRechteck = pygame.Rect(zombie.x+18,zombie.y+24,zombie.breite-36,zombie.hoehe-24)
    spielerRechteck = pygame.Rect(spieler.x+18,spieler.y+36,spieler.breite-36,spieler.hoehe-36)
 
    for k in kugeln:
        kugelRechteck = pygame.Rect(k.x-k.radius,k.y-k.radius,k.radius*2,k.radius*2)
        if zombieRechteck.colliderect(kugelRechteck):
            kugeln.remove(k)
            zombie.leben -= 1
            if zombie.leben <= 0 and not verloren:
                gewonnen = True
                pygame.mixer.Sound.play(siegSound)
                go = False
 
    if zombieRechteck.colliderect(spielerRechteck):
        verloren = True
        gewonnen = False
        pygame.mixer.Sound.play(verlorenSound)
        go = False
 
restart = True
while restart:
    linkeWand = pygame.draw.rect(screen, (0,0,0), (-2,0,2,600), 0)
    rechteWand = pygame.draw.rect(screen, (0,0,0), (1201,0,2,600), 0)

    spieler = Spieler(300,393,4,96,128,-16,[0,0,1,0],0,0, screen)
    zombie = Zombie(600,393,5,96,128,[0,0],40,1090,screen)
    
    verloren = False
    gewonnen = False
    kugeln = []

    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    
        spielerRechteck = pygame.Rect(spieler.x,spieler.y,96,128)
        gedrueckt = pygame.key.get_pressed()
    
        if gedrueckt[pygame.K_d] and not spielerRechteck.colliderect(rechteWand):
            spieler.laufen([0,1])
        elif gedrueckt[pygame.K_a] and not spielerRechteck.colliderect(linkeWand):
            spieler.laufen([1,0])
        else:
            spieler.stehen()
    
        if gedrueckt[pygame.K_q]:
            pause= False
            restart=False
            go = False

        if gedrueckt[pygame.K_w]:
            spieler.sprungSetzen()

        spieler.springen()
    
        if gedrueckt[pygame.K_SPACE]:
            if len(kugeln) <= 0 and spieler.ok:
                kugeln.append(Kugel(round(spieler.x),round(spieler.y),spieler.last,8,(0,0,0),7,screen))
            spieler.ok = False
    
        if not gedrueckt[pygame.K_SPACE]:
            spieler.ok = True
    
        kugelHandler()
        zombie.hinHer()
    
        kollision()
        zeichnen()
        clock.tick(60)
    
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        r = pygame.key.get_pressed()

        if r[pygame.K_r]:
            pause= False

        if r[pygame.K_q]:
            pause= False
            restart=False