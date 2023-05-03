import pygame
import sys
import webbrowser
from colorama import Fore,init
from SLLPygame import SingleLinkedList
from combo_box import ComboBox

class interface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Interface")
        self.SLL = SingleLinkedList()
        self.clicking = False
        self.flag_head = True
        self.Rect= pygame.Rect(0,60,1280,600)
        self.Rect2= pygame.Rect(20,90,1240,540)
        self.Rect3= pygame.Rect(45,482,1180,125)
        self.Rectcrab = pygame.Rect(396,180,72,64)
        self.Rectcat = pygame.Rect(547,180,72,64)
        self.Rectcrocodile = pygame.Rect(696,180,72,64)
        self.Rectdog = pygame.Rect(216,350,72,64)
        self.rectsheep = pygame.Rect(336,350,72,64)
        self.rectbutterfly = pygame.Rect(456,350,72,64)
        self.rectwhale = pygame.Rect(576,350,72,64)
        self.rectcat2 = pygame.Rect(696,350,72,64)
        self.rectcrab2 = pygame.Rect(816,350,72,64)
        self.rectcrocodile2 = pygame.Rect(936,350,72,64)
        self.sll_menu = pygame.Rect(35,15,90,40)
        self.dll_menu = pygame.Rect(230,15,90,40)
        self.pyc_menu = pygame.Rect(460,15,180,40)
        self.arbol_menu = pygame.Rect(780,15,130,40)
        self.grafo_menu = pygame.Rect(1060,15,120,40)
        self.rectgit = pygame.Rect(732,670,40,40)
        self.combo_box = pygame.Rect(400,282,250,15)
        self.combo_box_pos = pygame.Rect(900,282,250,15)
        self.list_pos = ["1"]
        self.combo = ComboBox(self.screen,["Agregar al principio","Agregar al final","Eliminar el primero","Eliminar el ultimo","Invertir lista","Eliminar todos los elementos","Eliminar por posición","Insertar por posición","Actualizar por posición","Eliminar nodos duplicados","Unir duplicados"],self.combo_box,"Black","Arial Black",15,4,"White","White",40," Seleccione una opcion")
        self.combo_pos = ComboBox(self.screen,self.list_pos,self.combo_box_pos,"Black","Arial Black",15,4,"White","White",40," Seleccione la posición")
        self.rectaux = pygame.Rect(0,0,0,0)
        self.rectaccept = pygame.Rect(1070,360,140,30)
        self.aux_node = None
        self.url ="https://github.com/JulianV122/data-structure"
        self.menu = "SLL"


#Crear Texto
    def create_text(self,font,text):
        new_text=font.render(text,0,(0,0,0))
        return new_text


#Mostrar todos los textos
    def show_text(self,text,x,y):
        self.screen.blit(text,(x,y))


#Guardar los textos
    def all_text(self):
        fuenteSistema = pygame.font.SysFont("Trebuchet MS",20)
        fuenteSistema2 = pygame.font.SysFont("Arial Black", 14)
        fuenteSistema3 = pygame.font.SysFont("Calibri", 18)
        fuenteSistema4 = pygame.font.SysFont("Arial",15)
        SLL = self.create_text(fuenteSistema,"SLL")
        DLL = self.create_text(fuenteSistema,"DLL")
        PYC = self.create_text(fuenteSistema,"PILAS Y COLAS")
        ARBOLES = self.create_text(fuenteSistema,"ARBOLES")
        GRAFOS = self.create_text(fuenteSistema,"GRAFOS")
        SingleLL = self.create_text(fuenteSistema2,"SINGLE LINKED LIST")
        Title = self.create_text(fuenteSistema3,"PARA INICIAR DEBES SELECCIONAR AL MENOS UNA IMAGEN QUE SERÁ LA CABEZA DE LA LISTA")
        SelMet = self.create_text(fuenteSistema3,"Selecciona un método:")
        SelPos = self.create_text(fuenteSistema3,"Selecciona la posición:")
        Estado = self.create_text(fuenteSistema3,">> Estado actual de la lista <<")
        Footer1 = self.create_text(fuenteSistema2,"Desarrollado por:")
        Footer2 = self.create_text(fuenteSistema4,"Julian Veloza")
        Footer3 = self.create_text(fuenteSistema4,"@ I SEM - 2023")
        ACEPTAR = self.create_text(fuenteSistema2,"ACEPTAR")
        self.show_text(SLL,75,25)
        self.show_text(DLL,270,25)
        self.show_text(PYC,500,25)
        self.show_text(ARBOLES,820,25)
        self.show_text(GRAFOS,1100,25)
        self.show_text(SingleLL,40,110)
        self.show_text(Title,260,150)
        self.show_text(SelMet,220,280)
        self.show_text(SelPos,700,280)
        self.show_text(Estado,200,450)
        self.show_text(Footer1,520,670)
        self.show_text(Footer2,655,672)
        self.show_text(Footer3,580,690)
        self.show_text(ACEPTAR,1100,366)


#Dibujar las imagenes en pantalla
    def draw_images(self):
        crab =pygame.image.load("Pygame/images/crab.png")
        cat =pygame.image.load("Pygame/images/cat.png")
        crocodile =pygame.image.load("Pygame/images/crocodile.png")
        dog =pygame.image.load("Pygame/images/dog.png")
        sheep =pygame.image.load("Pygame/images/sheep.png")
        butterfly =pygame.image.load("Pygame/images/butterfly.png")
        whale = pygame.image.load("Pygame/images/whale.png")
        logoUAM = pygame.image.load("Pygame/images/logoUAM.png")
        logoGit = pygame.image.load("Pygame/images/logoGit.png")
        iconLista = pygame.image.load("Pygame/images/iconLista.png")
        iconArbol = pygame.image.load("Pygame/images/iconArbol.png")
        iconGrafo =  pygame.image.load("Pygame/images/iconGrafo.png")
        self.screen.blit(logoUAM,(1165,662))
        self.screen.blit(logoGit,(732,670))
        self.screen.blit(crab,(400,180))
        self.screen.blit(cat,(550,180))
        self.screen.blit(crocodile,(700,180))
        self.screen.blit(dog,(220,350))
        self.screen.blit(sheep,(340,350))
        self.screen.blit(butterfly,(460,350))
        self.screen.blit(whale,(580,350))
        self.screen.blit(cat,(700,350))
        self.screen.blit(crab,(820,350))
        self.screen.blit(crocodile,(940,350))
        self.screen.blit(iconLista,(45,25))
        self.screen.blit(iconLista,(240,25))
        self.screen.blit(iconLista,(470,25))
        self.screen.blit(iconArbol,(790,25))
        self.screen.blit(iconGrafo,(1070,25))


#Dibujar rectangulos en pantalla
    def draw_screen(self):
        self.screen.fill("grey")
        pygame.draw.rect(self.screen,"black",self.Rect)
        pygame.draw.rect(self.screen,"grey",self.Rect2,border_radius=4)
        pygame.draw.rect(self.screen,"gray85",self.Rect3,border_radius=4)
        pygame.draw.rect(self.screen,"black",self.Rectcrab,2,0)
        pygame.draw.rect(self.screen,"black",self.Rectcat,2,0)
        pygame.draw.rect(self.screen,"black",self.Rectcrocodile,2,0)
        pygame.draw.rect(self.screen,"black",self.Rectdog,2,0)
        pygame.draw.rect(self.screen,"black",self.rectsheep,2,0)
        pygame.draw.rect(self.screen,"black",self.rectbutterfly,2,0)
        pygame.draw.rect(self.screen,"black",self.rectwhale,2,0)
        pygame.draw.rect(self.screen,"black",self.rectcat2,2,0)
        pygame.draw.rect(self.screen,"black",self.rectcrab2,2,0)
        pygame.draw.rect(self.screen,"black",self.rectcrocodile2,2,0)
        pygame.draw.rect(self.screen,"red",self.rectaux,2,0)
        pygame.draw.rect(self.screen,"gray70",self.sll_menu,-1,0)
        pygame.draw.rect(self.screen,"gray70",self.dll_menu,-1,0)
        pygame.draw.rect(self.screen,"gray70",self.pyc_menu,-1,0)
        pygame.draw.rect(self.screen,"gray70",self.arbol_menu,-1,0)
        pygame.draw.rect(self.screen,"gray70",self.grafo_menu,-1,0)
        pygame.draw.rect(self.screen,"black",self.combo_box,border_radius=3)
        pygame.draw.rect(self.screen,"black",self.combo_box_pos,border_radius=3)
        pygame.draw.rect(self.screen,"chartreuse3",self.rectaccept)
        pygame.draw.rect(self.screen,"Black",self.rectgit,-1,0)



#Mostrar las imagenes
    def draw_new_image(self):
        x=70
        y=510
        length=self.SLL.get_length_node()
        for i in range(1,length+1):
            if ( x < 1170):
                new_image =pygame.image.load(f"Pygame/images/{self.SLL.get_node_value(i)}.png")
                self.screen.blit(new_image,(x,y))
                x+=80


#CLick en la cabeza del nodo
    def is_click_head(self):
        mx,my = pygame.mouse.get_pos()
        loc = (mx,my)
        if self.clicking == True and self.flag_head == True and self.menu=="SLL":
            if self.Rectcat.collidepoint(loc):
                self.SLL.create_node_sll_unshift("cat")
                self.rectaux = self.Rectcat
                self.flag_head = False
                self.SLL.show_list()
            elif self.Rectcrab.collidepoint(loc):
                self.SLL.create_node_sll_unshift("crab")
                self.rectaux = self.Rectcrab
                self.flag_head = False
                self.SLL.show_list()
            elif self.Rectcrocodile.collidepoint(loc):
                self.SLL.create_node_sll_unshift("crocodile")
                self.rectaux = self.Rectcrocodile
                self.flag_head = False
                self.SLL.show_list()
        else:
            self.rectaux = pygame.Rect(0,0,0,0)


#Boton Aceptar
    def is_click_accept(self):
        if self.clicking == True and self.flag_head == False and self.menu == "SLL":
            if self.Rectdog.collidepoint(pygame.mouse.get_pos()):
                self.rectaux= self.Rectdog
                self.aux_node="dog"
            if self.rectsheep.collidepoint(pygame.mouse.get_pos()):
                self.rectaux= self.rectsheep
                self.aux_node="sheep"
            if self.rectbutterfly.collidepoint(pygame.mouse.get_pos()):
                self.rectaux= self.rectbutterfly
                self.aux_node="butterfly"
            if self.rectwhale.collidepoint(pygame.mouse.get_pos()):
                self.rectaux= self.rectwhale
                self.aux_node="whale"
            if self.rectcat2.collidepoint(pygame.mouse.get_pos()):
                self.rectaux= self.rectcat2
                self.aux_node="cat"
            if self.rectcrocodile2.collidepoint(pygame.mouse.get_pos()):
                self.rectaux= self.rectcrocodile2
                self.aux_node="crocodile"
            if self.rectcrab2.collidepoint(pygame.mouse.get_pos()):
                self.rectaux= self.rectcrab2
                self.aux_node="crab"

            if self.rectaccept.collidepoint(pygame.mouse.get_pos()):
                if self.combo.getIndex()==3:
                    self.aux_node=None
                    self.SLL.shift_node_sll()
                elif self.combo.getIndex()== 4:
                    self.aux_node=None
                    self.SLL.delete_node_sll_pop()
                elif self.combo.getIndex()== 5:
                    self.SLL.revert_node_list()
                    self.draw_new_image()
                elif self.combo.getIndex()==6:
                    self.SLL.remove_all_nodes()
                elif self.combo.getIndex() == 7 and self.combo_pos.getIndex != -1:
                    self.SLL.remove_node(self.combo_pos.getIndex())
                elif self.combo.getIndex()==10:
                    self.SLL.remove_duplicates()
                elif self.combo.getIndex()==11:
                    self.SLL.replace_list()
            if self.rectaccept.collidepoint(pygame.mouse.get_pos()) and self.aux_node is not None:
                if self.combo.getIndex() == -1:
                    return print("No se ha seleccionado ningún metodo")
                elif self.combo.getIndex() == 1:
                    self.SLL.create_node_sll_unshift(self.aux_node)
                    self.aux_node=None
                elif self.combo.getIndex()==2:
                    self.SLL.create_node_sll_ends(self.aux_node)
                    self.aux_node=None
                elif self.combo.getIndex()== 8 and self.combo.getIndex()!=-1:
                    self.SLL.insert_node(self.aux_node,self.combo_pos.getIndex())
                    self.aux_node=None
                elif self.combo.getIndex()== 9 and self.combo.getIndex()!=-1:
                    self.SLL.update_node_value(self.combo_pos.getIndex(),self.aux_node)
                    self.aux_node=None
            if self.SLL.length==0:
                self.flag_head=True
            self.SLL.show_list()

#Actualizar combo posición
    def update_combo_pos(self):
        if self.clicking == True and self.rectaccept.collidepoint(pygame.mouse.get_pos()):
            list_pos = [str(x) for x in range(1,self.SLL.get_length_node()+1)]
            self.combo_pos.updateOptions(list_pos)

#Abrir url github
    def open_url(self):
        if self.clicking == True:
            if self.rectgit.collidepoint(pygame.mouse.get_pos()):
                webbrowser.open_new(self.url)
        else:
            return None
        

#Validacion click menu
    def is_click_menu(self):
        if self.clicking==True:
            if self.sll_menu.collidepoint(pygame.mouse.get_pos()):
                self.menu="SLL"
            if self.dll_menu.collidepoint(pygame.mouse.get_pos()):
                self.menu="DLL"
            if self.arbol_menu.collidepoint(pygame.mouse.get_pos()):
                self.menu="ARBOL"
            if self.pyc_menu.collidepoint(pygame.mouse.get_pos()):
                self.menu="PYC"
            if self.grafo_menu.collidepoint(pygame.mouse.get_pos()):
                self.menu="GRAFO"

#Dibujar DLL
    def draw_DLL(self):
        pygame.draw.rect(self.screen,"black",self.Rect)
        pygame.draw.rect(self.screen,"grey",self.Rect2,border_radius=4)

#Dibujar arbol
    def draw_arbol(self):
        pygame.draw.rect(self.screen,"black",self.Rect)
        pygame.draw.rect(self.screen,"grey",self.Rect2,border_radius=4)

#Dibujar pyc
    def draw_pyc(self):
        pygame.draw.rect(self.screen,"black",self.Rect)
        pygame.draw.rect(self.screen,"grey",self.Rect2,border_radius=4)

#Dibujar grafo
    def draw_grafo(self):
        pygame.draw.rect(self.screen,"black",self.Rect)
        pygame.draw.rect(self.screen,"grey",self.Rect2,border_radius=4)



#Run
    def open_interface(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.clicking == False:
                        self.clicking=True
                        self.is_click_head()
                        self.is_click_accept()
                        self.open_url()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 :
                        self.clicking = False
            pygame.draw.rect(self.screen,"WHITE",(0,60,1280,600))
            self.is_click_menu()
            if self.menu=="SLL":
                self.draw_screen()
                self.all_text()
                self.draw_images()
                self.draw_new_image()
                self.combo_pos.draw()
                self.combo.draw()
                self.update_combo_pos()
            if self.menu=="DLL":
                self.draw_DLL()
            if self.menu=="ARBOL":
                self.draw_arbol()
            if self.menu=="GRAFO":
                self.draw_grafo()
            if self.menu=="PYC":
                self.draw_pyc()

            pygame.display.flip()


if __name__=="__main__":
    a= interface()
    a.open_interface()