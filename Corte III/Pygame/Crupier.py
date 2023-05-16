import pygame
from pilas import pilas
from Player import player

class crupier:
    def __init__(self,screen):
        self.screen = screen
        self.pilas = pilas(self.screen)
        self.baraja = self.pilas.shuffle_deck()
        self.player1 = player()
        self.player2 = player()
        self.player3 = player()
        self.player_crupier = player()
        self.players = [self.player1,self.player2,self.player3,self.player_crupier]
        self.crupier_score = self.player_crupier.score
        self.crupier_cards = self.player_crupier.cards
        self.player1.x=90
        self.player1.y=345
        self.player2.x= 540
        self.player2.y=400
        self.player3.x= 1014
        self.player3.y=345
        self.player_crupier.x=545
        self.player_crupier.y=238
        self.turn = 1
        self.click=False

    def asign_players_cards(self):
        for i in range(1,3):
            for player in self.players:
                if player != self.player_crupier:
                    card = self.baraja.pop()
                    player.add_card(card)
                    player.x+=30
        card = self.baraja.pop()
        card2 = self.baraja.pop()
        card2.reversed = True
        self.player_crupier.add_card(card)
        self.player_crupier.x+=30
        self.player_crupier.add_card(card2)
        self.player_crupier.x+=30
        
    def show_cards(self):
        for player in self.players:
            player.show_card()

    def turns(self,plantar1,plantar2,plantar3,pedir,start):
        if start is True:
            if self.turn == 1:
                if plantar1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self.click:
                    self.click=True
                    self.turn+=1
                elif pedir.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and self.players[self.turn-1].score <= 21 and not self.click:
                    self.click=True
                    self.request_letter(self.players[self.turn-1])
                if self.players[self.turn-1].score > 21:
                    self.turn+=1

            if self.turn == 2:
                if plantar2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self.click:
                    self.click=True
                    self.turn+=1
                elif pedir.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and self.players[self.turn-1].score <= 21 and not self.click:
                    self.click=True
                    self.request_letter(self.players[self.turn-1])
                if self.players[self.turn-1].score > 21:
                    self.turn+=1

            if self.turn == 3:
                if plantar3.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self.click:
                    self.click=True
                    self.turn+=1
                elif pedir.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and self.players[self.turn-1].score <= 21 and not self.click:
                    self.click=True
                    self.request_letter(self.players[self.turn-1])
                if self.players[self.turn-1].score > 21:
                    self.turn+=1

            if self.turn == 4:
                self.players[self.turn-1].cards[1].reversed = False
                if self.players[self.turn-1].score <= 16:
                    self.request_letter(self.players[self.turn-1])
                elif self.players[self.turn-1].score >= 17:
                    self.turn=0
            
            if self.turn == 0:
                for player in self.players:
                    self.status_player(player)

            if not pygame.mouse.get_pressed()[0]:
                self.click=False
            
            return self.turn

    def request_letter(self,player):
        card = self.baraja.pop()
        player.add_card(card)
        player.x+=30

    def status_player(self,player):
        if player.score <= 21 and player.score == self.player_crupier.score:
            player.status="EMPATE"
        elif player.score <= 21 and player.score > self.player_crupier.score :
            player.status="GANÓ"
        elif player.score <= 21 and self.player_crupier.score > 21:
            player.status="GANÓ"
        else:
            player.status="PERDIÓ"

