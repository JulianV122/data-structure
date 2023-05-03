class SingleLinkedList:

    class Node:
        def __init__(self,value):
            self.value= value
            self.next = None
    
    """ Por fuera de la clase de nodo"""
    def __init__ (self):
        self.head = None
        self.tail = None
        self.length = 0

    def show_list(self):
        #1. Declarar un array(lista) vacia que contendra los valores de los nodos de SL
        #array_with__nodes_value = []
        array_with_nodes_value = list()
        Current_node = self.head
        #Mientras con el nodo actual que estoy vistitando sea diferente de None
        while(Current_node!= None):
            #Añado el nodo actual que estoy visitando sea diferente de None
            array_with_nodes_value.append(Current_node.value)
            #current += 1 NO SIRVE PARA PASAR AL SIGUIENTE NODO DE UNA SLL
            #Pasamos del nodo actual al siguiente nodo mediante el puntero
            Current_node = Current_node.next
        #Imprimimos los valores de la lista
        print(f"Los valores de los nodos de la SLL son: \n {str(array_with_nodes_value)}")

    def create_node_sll_ends(self, value):
        #Creamos una variable qur va tener la estructura de un nodo
        new_node = self.Node(value)
        #Validar si la SLL tiene nodos o no
        """
        if self.length == 0:
            print("La lista simplemente enlazada no tiene nodos")
        else:
            print("La lista simplentente enlazada si tiene nodos")
        """
        
        if self.head == None:
            #Al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head = new_node
            self.tail = new_node
        else:
            #Si ingresa en esta condicion, es porque ya existe al menos un nodo
            #1. Debemos relacionar al nuevo nodo con la cola de la lista
            #2. Convertir al nuevo nodo en la cola de la lista
            self.tail.next = new_node
            self.tail = new_node
        #Incrementamos en 1 el tamaño de la lista
        self.length +=1

    def create_node_sll_unshift(self,value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            #1. Debemos relacionar al nuevo nodo con la cabeza de la lista
            #2. Convertir al nnuevo nodo en la cabeza de la lista
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def delete_node_sll_pop(self):
        #1. Validar si la lista esta vacia 
        #2. Validar si la lista tiene un unico nodo
        #3. Si tiene mas de un nodo eliminar el nodo que es la cola de la lista
        #4. Asignar al nodo anterior como la nueva cola de la lista
        if self.length == 0:
            print(">> Lista vacia no hay nodos por eliminar <<")
        elif self.length ==1:
            self.head = None
            self.tail = None
            self.length-=1
        else:
            #1. Recorrer la lista para identificar la cola 
            current_node= self.head
            """Nueva Linea"""
            new_tail = current_node
            while current_node.next != None:
                #3. Convertimos en la cola de la lista el nodo que actualmente estamos visitando
                new_tail = current_node
                #4. Pasamos al siguiente nodo antes de salir del while 
                current_node = current_node.next
            #5. Actualizamos la cola de la lista
            self.tail = new_tail
            self.tail.next = None
            #6. Reducimos en 1 el tamaño de la lista
            self.length -=1

    def shift_node_sll(self):
        if self.length == 0:
            print(">>Lista vacia no hay nodos por eliminar<<")
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length-=1
        else:
            #Actualizamos el nombre de la cabeza con la var aux
            remove_node = self.head
            print(f'Valor del nodo a eliminar es:({remove_node.value})')
            #Actualizamos la cabeza de la lista
            self.head = remove_node.next
            #eliminamos el enlace de remove_node con la lista
            remove_node.next= None
            self.length -= 1

    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while(index != node_counter):
                current_node =  current_node.next
                node_counter+=1
            return current_node
        
    def get_node_value(self, index):
        if index < 1 or index > self.length:
            print("No se encontro el nodo")
        elif index == 1:
            return self.head.value
        elif index == self.length:
            return self.tail.value
        else:
            current_node = self.head
            node_counter = 1
            while(index != node_counter):
                current_node =  current_node.next
                node_counter+=1
            return current_node.value
    
    def update_node_value(self, index,new_value):
        search_node = self.get_node(index)
        if search_node != None:
            #Encontro el nodo y se puede actualizar
            print(f'Actualizando el valor del nodo ...\n {search_node.value} por {new_value}')
            search_node.value = new_value
        else:
            #No se encuentra el nodo
            print(">>No se encontro el nodo")

    def remove_node(self,index):
        if index == 1:
            self.shift_node_sll()
        elif index == self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll = self.get_node(index)
            if remove_node_sll != None:
                previous_node = self.get_node(index - 1)
                print("Se va a eliminar: ",self.get_node(index).value)
                previous_node.next = remove_node_sll.next
                remove_node_sll.next = None
                self.length-=1
            else:
                print(" >>> No se encontro el nodo<<<")

    def remove_duplicates(self,value_to_remove):
        current_node= self.head
        next_node = current_node.next
        if self.find_duplicates(value_to_remove) > 1:
            while current_node != None:
                if current_node.value == value_to_remove:
                    index = self.get_node_index(current_node.value)
                    current_node=next_node
                    self.remove_node(index)
                else:
                    current_node=current_node.next

    def find_duplicates (self,value_duplicate):
        counter = 0
        current_node= self.head 
        while current_node != None:
            if current_node.value==value_duplicate:
                counter+=1
            current_node=current_node.next
        print (counter)
        return counter


    def get_length_node(self):
        return self.length
    
    def get_node_index(self,value):
        index = 1
        current_node= self.head
        while current_node!= None:
            if(current_node.value == value):
                return index
            else:
                current_node=current_node.next
                index+=1
        print("El valor no se encuentra")

    def revert_node_list(self):
        if self.length > 1:
            aux_head = self.tail
            aux_tail = self.head
            if self.length == 2:
                self.head = aux_head
                self.head.next = aux_tail
                self.tail = aux_tail
                self.tail.next = None
                return
            
            current_node = self.tail
            for i in range (1, self.length - 1):
                node = self.get_node(self.length - i)
                current_node.next = node
                current_node = node
            node.next = aux_tail
            self.head = aux_head
            self.tail = aux_tail
            self.tail.next=None


    def remove_all_nodes(self):
        self.head.next=None
        self.head=None
        self.tail=None
        self.length=0



    def verify_list(self):
        if self.length==0:
            print("Esta vacia")
        else:
            print(f"Tiene {self.length} elementos")

    def show_order_list(self):
        array_with_nodes_value = list()
        Current_node = self.head
        while(Current_node!= None):
            array_with_nodes_value.append(Current_node.value)
            Current_node = Current_node.next
        array_with_nodes_value.sort()
        print(f"Los valores de los nodos de la SLL son: \n {str(array_with_nodes_value)}")

    def insert_node(self,value,index):
        if index == 1:
            self.create_node_sll_unshift(value)
        elif index == self.length + 1:
            self.create_node_sll_ends(value)
        else:
            new_node = self.Node(value)
            actual_node_sll = self.get_node(index)
            if actual_node_sll != None:
                previous_node = self.get_node(index - 1)
                previous_node.next = new_node
                new_node.next = actual_node_sll
                self.length+=1
            else:
                print("No se puede acceder ")
        return True