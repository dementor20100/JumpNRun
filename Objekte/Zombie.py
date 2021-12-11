import pygame

class Zombie:
    def __init__(self,x,y,geschw,breite,hoehe,richtg,xMin,xMax,screen):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.richtg = richtg
        self.schritteRechts = 0
        self.schritteLinks = 0
        self.xMin = xMin
        self.xMax = xMax
        self.leben = 6
        self.linksListe = [pygame.image.load("Grafiken/l1.png"),pygame.image.load("Grafiken/l2.png"),pygame.image.load("Grafiken/l3.png"),pygame.image.load("Grafiken/l4.png"),pygame.image.load("Grafiken/l5.png"),pygame.image.load("Grafiken/l6.png"),pygame.image.load("Grafiken/l7.png"),pygame.image.load("Grafiken/l8.png")]
        self.rechtsListe = [pygame.image.load("Grafiken/r1.png"),pygame.image.load("Grafiken/r2.png"),pygame.image.load("Grafiken/r3.png"),pygame.image.load("Grafiken/r4.png"),pygame.image.load("Grafiken/r5.png"),pygame.image.load("Grafiken/r6.png"),pygame.image.load("Grafiken/r7.png"),pygame.image.load("Grafiken/r8.png")]
        self.ganz = pygame.image.load("Grafiken/voll.png")
        self.halb = pygame.image.load("Grafiken/halb.png")
        self.leer = pygame.image.load("Grafiken/leer.png")
        self.screen=screen

    def herzen(self):
        if self.leben >= 2:
            self.screen.blit(self.ganz, (507,15))
        if self.leben >= 4:
            self.screen.blit(self.ganz, (569,15))
        if self.leben == 6:
            self.screen.blit(self.ganz, (631,15))
 
        if self.leben == 1:
            self.screen.blit(self.halb, (507,15))
        elif self.leben == 3:
            self.screen.blit(self.halb, (569,15))
        elif self.leben == 5:
            self.screen.blit(self.halb, (631,15))
 
        if self.leben <= 0:
            self.screen.blit(self.leer, (507,15))
        if self.leben <= 2:
            self.screen.blit(self.leer, (569,15))
        if self.leben <= 4:
            self.screen.blit(self.leer, (631,15))
            
    def zeichnen(self):
        if self.schritteRechts == 63:
            self.schritteRechts = 0
        if self.schritteLinks == 63:
            self.schritteLinks = 0
 
        if self.richtg[0]:
            self.screen.blit(self.linksListe[self.schritteLinks//8], (self.x,self.y))
        if self.richtg[1]:
            self.screen.blit(self.rechtsListe[self.schritteRechts//8], (self.x,self.y))

    def Laufen(self):
        self.x += self.geschw
        if self.geschw > 0:
            self.richtg = [0,1]
            self.schritteRechts += 1
        if self.geschw < 0:
            self.richtg = [1,0]
            self.schritteLinks += 1
    def hinHer(self):
        if self.x > self.xMax:
            self.geschw *= -1
        elif self.x < self.xMin:
            self.geschw *= -1
        self.Laufen()