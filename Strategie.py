import pygame
import sys
import time
import random
from pygame.locals import*
xm = 0
ym = 0
laufzeit = 1
fenster = pygame.display.set_mode((1000,700))
displaygröße = (1200,700)
PB = 0
class display():
    def __init__(self):
        displaygröße = (1200,700)
        self.display = pygame.display.set_mode(displaygröße)
        
        self.display = pygame.display.set_mode((1000,600))
        self.display = fenster
        pygame.display.flip()
        self.uberschrift = pygame.display.set_caption("Strategiespiel")
        self.bild = pygame.image.load("x.bmp")
        if self.bild.get_alpha() == None:
            self.bild = self.bild.convert()
        else:
            self.bild = bild.convert_alpha()
        self.display.blit(self.bild, (0,0))
class Personen(object):
    def __init__(self,displaygröße):
        
        self.chx = 200
        self.chy = 100
        self.pos = (self.chx,self.chy)
        self.chx2 = int(self.chx + 100)
        self.chy2 = int(self.chy + 200)
        self.lp = 0
        self.gesch = 0
        self.beruf = ["Händler","Bauer","Soldat","Minenarbeiter"]
        self.punkte = 0
        self.rang = 0
        self.stimmung = 0
        self.display = pygame.display.set_mode((1000,600))
        self.display = fenster
        self.mw = ["Mann","Frau"]
        self.kosten = 0
        self.unter = 0
        self.richou = 0
        self.richlr = 0
        self.farbe = (0,0,255)
        self.höhe = 100
        self.breite = 200
        self.schaps = 0
        self.prd = 0
        self.rect = pygame.Rect(0, self.chy-int(self.höhe*0.5),self.breite,self.höhe)
        
    def update(self):
        self.chx += self.richlr*self.gesch        
        self.chy += self.richou*self.gesch
        self.rect.center = (self.chx,self.chy)
        if abs(self.chx - xm) <= self.chx2:
            PB = 1
        if abs(self.chy - ym) <= self.chy2:
            PB = 1
        
    def render(self, fenster):
        pygame.draw.rect(fenster, self.farbe,self.rect, 0)
        pygame.draw.rect(fenster, (0,0,255), self.rect, 1)
    

def Menu():
    display()
    fenster = pygame.display.set_mode((1000,600))
    TestP = Personen(displaygröße)
    xm = 0
    ym = 0
    mousepos = (xm,ym)
    
    while laufzeit:
        for event in pygame.event.get():
            
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = 1
                mousepos = event.pos
                mousepos = 0
                if PB == 1:
                    print(1)
            if event.type == pygame.MOUSEBUTTONUP:
                mousepos = 0
                mousepos = event.pos
            
            
                
        
        pygame.display.flip()
        display.uberschrift = pygame.display.set_caption("Strategie")
        bild = pygame.image.load("x.bmp")
        if bild.get_alpha() == None:
            bild = bild.convert()
        else:
            bild = bild.convert_alpha()
        fenster.blit(bild, (0,0))
        
        

        TestP.update()
        
        TestP.render(fenster)         
Menu()







