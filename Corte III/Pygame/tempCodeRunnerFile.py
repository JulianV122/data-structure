import pygame
import random
from collections import deque


class pilas:
    def __init__(self,screen):
        self.screen = screen
        self.baraja = []
        self.cartas = ["AS","1","2","3","4","5","6","7","8","9","10","J","K","Q"]
    

    def shuffle_deck(self):
        for i in range(1,52):
            self.baraja.append(random.choice(self.cartas))
        print(self.baraja)