import pygame 
import sys
from game import game
class main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("Menu")
        self.rect1= pygame.Rect(415,245,400,80)
        self.rect2=pygame.Rect(415,355,400,80)
        self.select="menu"
        self.game = game(self.screen)
        self.clicking = False

    def draw_screen(self):
        if self.select=="menu":
            self.screen.fill("darkcyan")
            pygame.draw.rect(self.screen,"cyan3",self.rect1,0,2)
            pygame.draw.rect(self.screen,"cyan3",self.rect2,0,2)
        if self.select=="game":
            self.game.draw_screen_game()


    def create_text(self,font,text):
        new_text=font.render(text,0,"Black")
        return new_text
    
    def show_text(self,text,x,y):
        self.screen.blit(text,(x,y))

    def draw_text(self):
        if self.select=="menu":
            font1= pygame.font.SysFont("Lucida Console",65)
            font2= pygame.font.SysFont("Lucida Console",80)
            start= self.create_text(font1,"START GAME")
            quitgame = self.create_text(font1,"QUIT GAME")
            title = self.create_text(font2,"SOLITAIRE GAME")
            self.show_text(start,420,250)
            self.show_text(quitgame,435,360)
            self.show_text(title,310,40)
        

    def is_click(self):
        if self.clicking==True:
            if self.rect1.collidepoint(pygame.mouse.get_pos()):
                self.select="game"
                pygame.display.set_caption("Game")
            if self.rect2.collidepoint(pygame.mouse.get_pos()):
                sys.exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.clicking == False:
                        self.clicking=True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 :
                        self.clicking = False
            self.draw_screen()
            self.draw_text()
            self.is_click()
            pygame.display.flip()

if __name__=="__main__":
    a= main()
    a.run()