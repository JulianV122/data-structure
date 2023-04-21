'''
    List methods
    Date: 27/01/23
'''
class ListMethods:
    def __init__(self):
        #1. Definimos una lista vacia 
        self.pets=[]
        self.vehicles = list()

    #2. Metodo para añadir elementos en la lista
    def add_list_elements(self):
        # ['Dog','cat']
        self.pets.append("dog")
        self.pets.append("cat")
        print(self.pets)    
    #3. Metodo que solicita valores al usuario
    def input_data_vehicles_list(self):
        #Variables locales: vehciles_number; vehicles_ty
        vehicles_number = int(input("Cuantos vehiculos tienes: "))
        #Recorrer una lista 
        for vehicle_item in range(vehicles_number):
            vehicle_type = input("tipo de vehiculo: ")
            #añadomos elementos a la lista
            self.vehicles.append(vehicle_type)
        
        #Imprimir toda la lista
        print(self.vehicles)
        #Imprimir ultimo, penultimo, y antepenultimo elemento de la lista
        print(self.vehicles[-1],self.vehicles[-2],self.vehicles[-3])
    
    #4 Extraer valores de una lista
    def show_collection_data_list(self):
        #imprimir desde la posicion 2 hasta 3
        print(self.vehicles[2:4])
        #Todos los elementos de la lista
        print(self.vehicles[:])
        #Elementos desde un indice especifico: 2 [2,3,...]
        print(self.vehicles[2:])
        #Elementos hasta un indice especifico : 2 [0,1,2]
        print(self.vehicles[:2])
        #Acceder a los elementos de 2 en 2
        print(self.vehicles[::2])
        #Acceder a un SUBCONJUNTO de elementos de 2 en 2
        print(self.vehicles[1:5:2])

    #5. Iterar los elemeentos de una lista con for
    def iteration_list(self):
        for item in self.vehicles:
            print(item)
        #Validar si la lista contiene un valor especifico
        if "Carro".capitalize in self.vehicles:
            print("Si se encontro valor")
        else:
            print("No se encontro el valor")

    #6 Añadir varios elementos al final de la lista
    def add_elements(self):
        self.vehicles.extend(["Avion","Tractomula","Otro medio"])
        print(self.vehicles)
    
    #7 Añadir un elemento en posicion especifica de la lista
    def add_specific_element(self):
        self.vehicles.insert(0,"Moto")
        print(self.vehicles)

    #8 Eliminar un elemento 
    def remove_last_element(self):
        self.vehicles.pop()
        print(self.vehicles)
    
    #9 ELiminar elemento de posicion especifica 
    def remove_specific_element(self):
        #primer elemento
        self.vehicles.pop(0)
        print(self.vehicles)

    #10 Eliminar todos los valores de la lista
    def remove_all_elements(self):
        self.vehicles.clear()

    #11 Eliminar de la lista un valor especifico
    def remove_element_by_name(self):
        self.vehicles.remove("tractomula".capitalize())
        print(self.vehicles)
    
    #12. Eliminar todas las coincidencias de valor en la lista
    def remove_all_elements_match(self):
        new_list = list(filter(("tractomula".capitalize()).__ne__,self.vehicles))
        print(new_list)



