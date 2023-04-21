from random import sample
from colorama import Fore, init
init()

class SortAlgorithms:
    def __init__(self):
        self.number_list = range(100)
        self.list_bubble_sort = sample(self.number_list,8)
        self.list_select_sort = sample(self.number_list,8)
        self.list_insert_sort = sample(self.number_list,8)
        self.list_merge_sort = sample(self.number_list,8)
        self.list_quick_sort = sample(self.number_list,8)
        self.list_radix_sort = sample(self.number_list,8)

    #Ordenamiento burbuja
    def bubble_sort_function(self):
        #Comparacion por pares, iniciamos comparando los 2 primeros elementos
        print(Fore.CYAN+"--------------------------------------------------"+Fore.RESET)
        print(Fore.GREEN + "               Ordenamiento burbuja"+Fore.RESET)
        #Crear un contador para conocer la cantidad de elementos de la lista
        count_item_list = 0
        for i in self.list_bubble_sort:
            # Al contador de elementos, cada vez que visitemos una posicion le sumamos
            count_item_list += 1
        print(self.list_bubble_sort)
        #Recorremos la lista e iniciamos la comparacion de valor
        print("Primer for contador-1: ",count_item_list-1)
        for j in range(count_item_list-1):
            print(Fore.RED + f'{j}' + Fore.RESET)
            for k in range (count_item_list - j - 1):
                print(Fore.BLUE + f'{k}' + Fore.RESET)
                #Comparamos el valor de la posicion actual con el valor de la sgte
                if self.list_bubble_sort[k] > self.list_bubble_sort[k+1]:
                    # Transposicion de valores 
                    self.list_bubble_sort[k], self.list_bubble_sort[k+1]=self.list_bubble_sort[k+1],self.list_bubble_sort[k]
        print(self.list_bubble_sort)

    def bubble_sort_function_refactor(self):
        change_position = True
        while change_position:
            change_position = False
            for i in range (len(self.list_bubble_sort)-1):
                if self.list_bubble_sort[i] > self.list_bubble_sort[i+1]:
                    self.list_bubble_sort[i], self.list_bubble_sort[i+1] = self.list_bubble_sort[i+1],self.list_bubble_sort[i]
                    change_position = True
        print(self.list_bubble_sort)

    def select_sort_function(self):
        print(Fore.CYAN+"--------------------------------------------------"+Fore.RESET)
        print(Fore.GREEN + "               Ordenamiento seleccion "+Fore.RESET)
        count_item_list = 0
        # Inicializamos contador
        for i in self.list_select_sort:
            count_item_list +=1
        
        # Recorremos la lista y generamos la comparacion de valores entre posiciones 
        for i in range(count_item_list):
            min = i
            print(Fore.RED + f'{i}' + Fore.RESET)
            for j in range(i+1,count_item_list):
                print(Fore.BLUE + f'{j}' + Fore.RESET)
                #Comparacion de valores 
                print("Comparacion " + str(self.list_select_sort[min])+" - "+str(self.list_select_sort[j]))
                if  self.list_select_sort[min] > self.list_select_sort[j]:
                    min=j
            #Generamos el intercambio, la transposición 
            self.list_select_sort[i], self.list_select_sort[min] = self.list_select_sort[min], self.list_select_sort[i]
        print(self.list_select_sort)
        
    def insert_sort_function(self):
        print(Fore.CYAN+"--------------------------------------------------"+Fore.RESET)
        print(Fore.GREEN + "               Ordenamiento de inserción "+Fore.RESET)
        print(self.list_insert_sort)
        #Separamos la lista en dos partes(puede o no estar) ordenados
        for i in range (1, len(self.list_insert_sort)):
            item_visited = self.list_insert_sort[i]
            #Visitamos la posicion anterior al actual
            j = i - 1
            # Todos los elementos de valor mayor pasan adelante 
            while j>=0 and self.list_insert_sort[j]>item_visited:
                print(Fore.CYAN + str(self.list_insert_sort[j])+Fore.RESET+" > "+str(item_visited))
                self.list_insert_sort[j+1]=self.list_insert_sort[j]
                j -=1
                #Transposicion
            self.list_insert_sort[j+1]=item_visited
            print(self.list_insert_sort)

    def quick_sort_function(self):
        """
        Ordena una lista de forma recursiva utilizando el algoritmo QuickSort

        Args:
        - arr: Lista a ordenar

        Returns:
        - Lista ordenada
        """

        # Caso base: si la lista tiene menos de 2 elementos, ya está ordenada
        if len(self) < 2:
            return self

        # Elegir un elemento pivote
        # En este caso, elegimos el elemento del medio de la lista
        # Esto es una mejora respecto a elegir siempre el primer elemento
        # Puede reducir el riesgo de que QuickSort tenga un peor rendimiento en listas preordenadas
        pivot_index = len(self) // 2
        pivot = self[pivot_index]

        # Dividir la lista en dos sublistas, una de elementos menores que el pivote y otra de elementos mayores o iguales al pivote
        # En lugar de crear dos nuevas listas, utilizamos dos índices (left y right) para mantener los elementos en la misma lista
        left, right = 0, len(self) - 1
        while left <= right:
            if self[left] < pivot:
                left += 1
            elif self[right] >= pivot:
                right -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        # Recursivamente ordenar las sublistas izquierda y derecha
        # En lugar de crear dos nuevas listas, simplemente utilizamos slices (rebanadas) de la lista original
        # También agregamos un check para evitar llamar a quick_sort() en una sublista vacía (lo que produciría un error)
        sorted_left = quick_sort(arr[:pivot_index]) if pivot_index > 0 else []
        sorted_right = quick_sort(arr[pivot_index:]) if pivot_index < len(arr) - 1 else []

        # Combinar las sublistas izquierda, pivote y derecha en una sola lista
        return sorted_left + [pivot] + sorted_right
