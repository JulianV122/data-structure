import pygame
from Crupier import crupier

class blackjack:
    def __init__(self,screen):
        self.screen = screen
        self.rectStart = pygame.Rect(309,88,92,34)
        self.rectRestart = pygame.Rect(309,140,92,34)
        self.rectPedirCarta = pygame.Rect(800,265,100,34)
        self.rectPlantarmeJ1=pygame.Rect(192,463,92,34)
        self.rectPlantarmeJ2=pygame.Rect(642,530,92,34)
        self.rectPlantarmeJ3=pygame.Rect(1126,463,92,34)
        self.crupier = crupier(self.screen)
        self.initial = False
        self.turn = 0
        
    def drawText(self, text, color, font, size, x, y):
        font_type = pygame.font.SysFont(font, size)
        new_text = font_type.render(text, False, color)
        self.screen.blit(new_text, (x, y))

    def draw_images_blackjack(self):
        background = pygame.image.load("Corte III/Pygame/pilasImages/background.jpg")
        crupier = pygame.image.load("Corte III/Pygame/pilasImages/crupier.png")
        baraja = pygame.image.load("Corte III/Pygame/pilasImages/Baraja.png")
        self.screen.blit(background,(0,60))
        self.screen.blit(crupier,(560,78))
        self.screen.blit(baraja,(786,153))
        if self.initial == True:
            self.crupier.show_cards()
        
    def show_text_blackjack(self):
        self.drawText("PRESIONA START PARA EMPEZAR EL JUEGO","White","Arial",16,15,95)
        self.drawText("JUGADOR 1  ","White","Arial",20,54,473)
        self.drawText("START","White","Arial",20,328,94)
        self.drawText("JUGADOR 2","White","Arial",20,508,537)
        self.drawText("PLANTARME","White","Arial",16,198,473)
        self.drawText("PLANTARME","White","Arial",16,650,538)
        self.drawText("JUGADOR 3","White","Arial",20,990,473)
        self.drawText("PLANTARME","White","Arial",16,1130,473)
        self.drawText("PEDIR CARTA","White","Arial",16,803,273)
        self.drawText("RESTART","White","Arial",20,320,145)
        self.drawText(self.crupier.player1.status,"White","Arial",16,130,303)
        self.drawText(self.crupier.player2.status,"White","Arial",16,583,372)
        self.drawText(self.crupier.player3.status,"White","Arial",16,1060,303)

        if self.turn == 1:
            self.drawText("JUGADOR 1  ","Red","Arial",20,54,473)
        
        if self.turn == 2:
            self.drawText("JUGADOR 2","Red","Arial",20,508,537)

        if self.turn == 3:
            self.drawText("JUGADOR 3","Red","Arial",20,990,473)


    def draw_rect_blackjack(self):
        pygame.draw.rect(self.screen,"Orange",self.rectStart)
        pygame.draw.rect(self.screen,"Orange",self.rectPedirCarta)
        pygame.draw.rect(self.screen,"Orange",self.rectPlantarmeJ1)
        pygame.draw.rect(self.screen,"Orange",self.rectPlantarmeJ2)
        pygame.draw.rect(self.screen,"Orange",self.rectPlantarmeJ3)
        pygame.draw.rect(self.screen,"Orange",self.rectRestart)


    def all_functions_blackjack(self):
        self.draw_images_blackjack()
        self.draw_rect_blackjack()
        self.show_text_blackjack()
        self.is_start()
        self.game()
        self.is_restart()

    def is_start(self):
        if self.rectStart.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self.initial:
            self.initial=True 
            self.crupier.asign_players_cards()

    def is_restart(self):
        if self.rectRestart.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and self.initial:
            self.crupier.empty_cards()

    def game(self):
        self.turn=self.crupier.turns(self.rectPlantarmeJ1,self.rectPlantarmeJ2,self.rectPlantarmeJ3,self.rectPedirCarta,self.initial)



