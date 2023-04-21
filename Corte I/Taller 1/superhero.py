from colorama import init
init()

class SuperHero():
    def __init__ (self):
        self.superheros_list=[]
        self.superpower_list=[]
        self.creators_list=[]
        self.marvel_world=[]
        self.dc_world=[]
        self.superhero_name=""
        self.menu_option = 0
        self.world_menu = 0

    def initial_menu(self):
        print("Seleccione una opcion del menú: ")
        while True:
            try:
                self.menu_option = int(input(" 1.Agregar Superheroe \n 2.Buscar superheroe \n 3.Eliminar superheroe \n 4.Superheroe con mas superpoderes \n 5.Superheroe con menos superpoderes \n 6. Mostrar La lista de DC y Marvel \n 7.Salir del menú\n"))
                if self.menu_option < 1 or self.menu_option > 7:
                    print("Opcion incorrecta")
                elif self.menu_option == 1:
                    self.superhero_menu()
                elif self.menu_option == 2:
                    self.search_superhero()
                elif self.menu_option == 3:
                    self.remove_superhero()
                elif self.menu_option == 4:
                    self.most_superpowers()
                elif self.menu_option == 5:
                    self.less_superpowers()
                elif self.menu_option == 6:
                    self.show_superheroes_list()
                elif self.menu_option == 7:
                    break
            except ValueError:
                print(">>Se esperaba un numero<<")

    def superhero_menu(self):
        print("Seleccione Universo del Superheroe: ")
        while True:
            try:
                self.world_menu= int(input(" 1. Marvel \n 2. DC \n 3. Salir\n"))
                if self.world_menu < 1 or self.world_menu > 3:
                    print("Opcion incorrecta")
                elif self.world_menu == 1:
                    self.input_superhero_data()
                elif self.world_menu == 2:
                    self.input_superhero_data()
                elif self.world_menu == 3:
                    break
            except ValueError:
                print(">>Se esperaba un numero<<")



    def input_superhero_data(self):
        while True:
            try:
                superhero_number=int(input("Cuantos superheroes desea añadir:"))
                for superhero in range(superhero_number):
                    superpower_list=[]
                    creators_list=[]
                    self.superhero_name=input("Ingrese nombre del superheroe: ").capitalize()
                    superpowers_number=int(input("Cantidad de superpoderes: "))
                    for superpower in range(superpowers_number):
                        superpower_list.append(input("Ingrese superpoder: ").capitalize())
                    creators_number=int(input("Ingrese cantidad de creadores: "))
                    for creators in range(creators_number):
                        creators_list.append(input("Ingrese Creador: ").capitalize())
                    self.superheros_list.append((self.superhero_name,superpower_list,creators_list))
                    if self.world_menu == 1:
                        self.marvel_world.append((self.superhero_name,superpower_list,creators_list))
                    elif self.world_menu == 2:
                        self.dc_world.append((self.superhero_name,superpower_list,creators_list))
                        self.superheros_list.remove()
                print("Marvel: ")
                print(self.marvel_world)
                print("DC: ")
                print(self.dc_world)
                break
            except ValueError:
                print(">>Se esperaba un numero<<")
            

    def search_superhero(self):
        superhero_name=input("Ingrese nombre del superheroe para buscar: ").capitalize()
        flag=False
        for superhero in self.superheros_list:
            if superhero_name in superhero[0]:
                print(superhero_name)
                print(superhero[1])
                flag=True
            
        if not flag:
            print("No se encontró el superheroe")
            user_ask=int(input("Desea añadir el superheroe? \n 1.si\n 2.no \n"))
            if user_ask==1:
                self.superhero_menu()

    
    def remove_superhero(self):
        superhero_name=input("Ingrese nombre del superheroe a eliminar: ").capitalize()
        flag = False
        for superhero in self.marvel_world:
            if superhero_name in superhero[0]:
                self.marvel_world.remove(superhero)
                print(self.marvel_world)
                print("Removido con exito")
        for superhero in self.dc_world:
            if superhero_name in superhero[0]:
                self.dc_world.remove(superhero)
                print(self.dc_world)
                print("Removido con exito")
        for superhero in self.superheros_list:
            if superhero_name in superhero[0]:
                self.superheros_list.remove(superhero)
                print("Marvel: ")
                print(self.marvel_world)
                print("DC: ")
                print(self.dc_world)
                flag=True
        if not flag:
            print("No se encontró el superheroe para eliminar")


    def most_superpowers(self): 
        superhero_name=""
        number=0
        for superhero in self.superheros_list:
            if len(superhero[1])>number:
                number=len(superhero[1])
                superhero_name=str(superhero[0])
                print("Superheroe con mas superpoderes: "+superhero_name)
            else:
                print("No hay superheroes")

    def less_superpowers(self): 
        superhero_name=""
        number=99
        for superhero in self.superheros_list:
            if len(superhero[1])<number:
                number=len(superhero[1])
                superhero_name=str(superhero[0])
        print("Superheroe con mas superpoderes: "+superhero_name)
    
    def show_superheroes_list(self):
        print(self.superheros_list)