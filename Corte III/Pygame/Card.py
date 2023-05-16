import pygame

class cards:
    def __init__(self,screen,name):
        self.screen = screen
        self.name = name
        self.value = self.asign_value()
        self.x = 0
        self.y = 0
        self.reversed = False
        
    def asign_value(self):
        if self.name == "2":
            self.value = 2
        if self.name == "3":
            self.value = 3
        if self.name == "4":
            self.value = 4
        if self.name == "5":
            self.value = 5
        if self.name == "6":
            self.value = 6
        if self.name == "7":
            self.value = 7
        if self.name == "8":
            self.value = 8
        if self.name == "9":
            self.value = 9
        if self.name == "10":
            self.value = 10
        if self.name == "K" or self.name == "Q" or self.name=="J":
            self.value = 10
        if self.name == "AS":
            self.value = 11

    
    def set_value(self,value):
        self.value = value

    def draw_card(self):
        if self.reversed is False:
            card_image = pygame.image.load(f"Corte III/Pygame/pilasImages/{self.name}.png")
        else:
            card_image = pygame.image.load(f"Corte III/Pygame/pilasImages/R.png")
        self.screen.blit(card_image,(self.x,self.y))
