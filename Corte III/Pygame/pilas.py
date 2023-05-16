import pygame
import random
from Card import cards

class pilas:
    def __init__(self,screen):
        self.screen = screen
        self.cartas = ["AS","2","3","4","5","6","7","8","9","10","J","K","Q"]
    
    def shuffle_deck(self):
        baraja = []
        for i in range(1,52):
            card=cards(self.screen,random.choice(self.cartas))
            baraja.append(card)
        return baraja
        
    def asign_value (self,card):
        card.asign_value()
