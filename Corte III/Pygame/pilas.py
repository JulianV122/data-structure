import pygame
from collections import deque


class pilas:
    def __init__(self,screen):
        self.screen = screen
        self.historial = deque()
        self.baraja = []
    


    def draw_images_pilas(self):
        background = pygame.image.load("Corte III/Pygame/pilasImages/background.jpg")
        self.screen.blit(background,(0,60))