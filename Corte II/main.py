import pygame, sys
from combo_box import ComboBox
pygame.init()

class Superheroes():
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Superheroes")
        self.BLACK   = (0  , 0  ,   0)
        self.WHITE   = (255, 255, 255)
        self.GREEN   = (134, 181, 129)
        self.RED     = (255, 0  ,   0)
        self.BLUE    = (0  , 0  , 255)
        self.GRAY    = (170, 170, 170)
        self.LIGHT_BLUE = (161, 163, 212)


        self.combo_rect = pygame.Rect(280, 109, 350, 50)
        self.combo = ComboBox(self.screen, ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5"], self.combo_rect, self.BLACK, "Arial", 22, 5, self.WHITE, self.WHITE, 40, "Seleccione una opción")
        self.button = pygame.Rect(504, 356, 191, 39)
        self.click_button = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.WHITE)
            pygame.draw.rect(self.screen, self.BLACK, self.combo_rect, 0, 5)
            self.combo.draw()
            self.drawButton("Aceptar", self.GRAY, self.button, 0, 16, 22, True, self.BLACK, "Consolas")
            self.clickOnButton()
            pygame.display.flip()
    
    def drawButton(self, text, button_color, background_rect, border, border_radius, text_size, text_bold, text_color, text_font):
        pygame.draw.rect(self.screen, button_color, background_rect, border, border_radius)
        font = pygame.font.SysFont("Arial", text_size, text_bold)
        render_text = font.render(text, True, text_color, None)
        self.screen.blit(render_text, (background_rect.x + (background_rect.width - render_text.get_width())/2, background_rect.y + (background_rect.height - render_text.get_height())/2))

    def clickOnButton(self):
        if self.button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == True and not self.click_button:
                print(self.combo.getValue())
                self.click_button = True
        if not pygame.mouse.get_pressed()[0]:
            self.click_button = False

if __name__ == '__main__':
    a = Superheroes()
    a.run()
