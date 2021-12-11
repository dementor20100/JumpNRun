import pygame

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