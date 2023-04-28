
class BinaryTree:
    #El constructor del árbol necesita el valor del nodo e indentificar el subárbol

    def __init__(self,value):
        self.value = value
        self.left_node= None
        self.right_node = None

    #Insertar un nodo en el árbol
    def insert(self,root,node):
        #Si no existe raíz en el arbol 
        if root is None:
            root= node
        else:
            #Si el valor del nodo es menor que el valor de la raíz 
            if root.value > node.value:
                #Si no existe nodo izquierdo
                if root.left_node is None:
                    root.left_node = node
                else:
                    #Si existe nodo izquierdo, se inserta el nodo en el subarbol izquierdo
                    self.insert(root.left_node,node)
            else:
                #Si no existe nodo derecho
                if root.right_node is None:
                    root.right_node = node
                else:
                    #Si existe nodo derecho se inserta el nodoen el subárbol derecho
                    self.insert(root.right_node,node)
            
    
    def print_tree (self,root):
        if root is not None:
            self.print_tree(root.left_node)
            print(root.value)
            self.print_tree(root.right_node)
