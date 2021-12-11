import pygame

class spieler:
    def __init__(self,x,y,geschw,breite,hoehe,sprungvar,richtg,schritteRechts,schritteLinks):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.sprungvar = sprungvar
        self.richtg = richtg
        self.schritteRechts = schritteRechts
        self.schritteLinks = schritteLinks
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
            pygame.mixer.Sound.play(sprungSound)
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
    def spZeichnen(self):
        if self.schritteRechts == 63:
            self.schritteRechts = 0
        if self.schritteLinks == 63:
            self.schritteLinks = 0
 
        if self.richtg[0]:
            screen.blit(linksGehen[self.schritteLinks//8], (self.x,self.y))
            self.last = [1,0]
 
        if self.richtg[1]:
            screen.blit(rechtsGehen[self.schritteRechts//8], (self.x,self.y))
            self.last = [0,1]
 
        if self.richtg[2]:
            if self.last[0]:
                screen.blit(angriffLinks, (self.x,self.y))
            else:
                screen.blit(angriffRechts, (self.x,self.y))
 
        if self.richtg[3]:
            screen.blit(sprung, (self.x,self.y))