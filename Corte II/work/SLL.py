class SLL:
    class Node:
        def __init__(self,value):
                self.value=value 
                self.next=None
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def agregar_al_final(self,value):
        new_node=self.Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def show_list(self):
        
        current_node=self.head
        if self.length==0:
            print("Lista Vacia")
        else:
            Array=[]
            while current_node!= None:
                Array.append(current_node.value*2)
                current_node=current_node.next
        print(Array)

