import pygame

class Spieler:
    def __init__(self,x,y,geschw,breite,hoehe,sprungvar,richtg,schritteRechts,schritteLinks,screen):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.sprungvar = sprungvar
        self.richtg = richtg
        self.schritteRechts = schritteRechts
        self.schritteLinks = schritteLinks
        self.soundSprung = pygame.mixer.Sound("Sounds/sprung.wav")
        self.bildSprung = pygame.image.load("Grafiken/sprung.png")
        self.bildRechtsGehen = [pygame.image.load("Grafiken/rechts1.png"),pygame.image.load("Grafiken/rechts2.png"),pygame.image.load("Grafiken/rechts3.png"),pygame.image.load("Grafiken/rechts4.png"),pygame.image.load("Grafiken/rechts5.png"),pygame.image.load("Grafiken/rechts6.png"),pygame.image.load("Grafiken/rechts7.png"),pygame.image.load("Grafiken/rechts8.png")]
        self.bildLinksGehen = [pygame.image.load("Grafiken/links1.png"),pygame.image.load("Grafiken/links2.png"),pygame.image.load("Grafiken/links3.png"),pygame.image.load("Grafiken/links4.png"),pygame.image.load("Grafiken/links5.png"),pygame.image.load("Grafiken/links6.png"),pygame.image.load("Grafiken/links7.png"),pygame.image.load("Grafiken/links8.png")]
        self.bildLinksAngriff = pygame.image.load("Grafiken/angriffLinks.png")
        self.bildRechtsAngriff = pygame.image.load("Grafiken/angriffRechts.png")
        self.screen=screen
        self.sprung = False
        self.last = [1,0]
        self.ok = True
    def laufen(self,liste):
        if liste[0]:
            self.x -= self.geschw
            self.richtg = [1,0,0,0]
            self.schritteLinks += 1
        if liste[1]:
            self.x += self.geschw
            self.richtg = [0,1,0,0]
            self.schritteRechts += 1
    def resetSchritte(self):
        self.schritteLinks = 0
        self.schritteRechts = 0
    def stehen(self):
        self.richtg = [0,0,1,0]
        self.resetSchritte()
    def sprungSetzen(self):
        if self.sprungvar == -16:
            self.sprung = True
            self.sprungvar = 15
            pygame.mixer.Sound.play(self.soundSprung)
    def springen(self):
        if self.sprung:
            self.richtg = [0,0,0,1]
            if self.sprungvar >= -15:
                n = 1
                if self.sprungvar < 0:
                    n = -1
                self.y -= (self.sprungvar**2)*0.17*n
                self.sprungvar -= 1
            else:
                self.sprung = False
    def zeichnen(self):
        if self.schritteRechts == 63:
            self.schritteRechts = 0
        if self.schritteLinks == 63:
            self.schritteLinks = 0
 
        if self.richtg[0]:
            self.screen.blit(self.bildLinksGehen[self.schritteLinks//8], (self.x,self.y))
            self.last = [1,0]
 
        if self.richtg[1]:
            self.screen.blit(self.bildRechtsGehen[self.schritteRechts//8], (self.x,self.y))
            self.last = [0,1]
 
        if self.richtg[2]:
            if self.last[0]:
                self.screen.blit(self.bildLinksAngriff, (self.x,self.y))
            else:
                self.screen.blit(self.bildRechtsAngriff, (self.x,self.y))
 
        if self.richtg[3]:
            self.screen.blit(self.bildSprung, (self.x,self.y))