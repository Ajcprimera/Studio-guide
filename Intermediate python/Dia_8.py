#Linked list
'''
Las estructuras linked consisten en nodos conectados a otros nodos, los más comunes 
son sencillos o dobles. No se accede por índice sino por recorrido. 
Es decir se busca en la lista de nodos hasta encontrar un valor.
'''

'''
Nodo: es un bloque de espacio en memoria que almacena un dato o datos
'''

#metodo para crear la clase nodo
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

#Nota: los nodos no son secuenciales

if __name__ == '__main__':
    node1 = None
    node2 = Node('A', None)
    node3 = Node('B', node2)
    print(node2.data)
    print(node2.next)
    print(node3.next)
    print(node3.next.data)

    #Creando nodos de manera iterativa
    head = None
    for i in range(1,5):
        head = Node(i, head)

    while head != None:
        print(head.data)
        head = head.next

#Single linked list

'''
Es una coleccion lineal de nodos
'''

class Node2:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def append(self, value):
        myNode = Node2(value)
        if self.size == 0:
            self.first = myNode
        else:
            current = self.first
            while current.next != None:
                current = current.next
            current.next = myNode
        
        self.size +=1
        return myNode
    
    '''El metodo delete, no es del todo eliminar el nodo,
    lo que hacemos es redireccionar el puntero del nodo hacia
    el siguiente del sgte y de esa manera resstructurar la linked list
    '''
    def delete(self, value):
        if self.size == 0:
            return False
        else:
            current = self.first
            try:
                while current.next.value != value:
                    current = current.next
                removeNode = current.next
                current.next = removeNode.next
            except AttributeError:
                return False

            
        self.size -= 1

        return removeNode
    
    def __len__ (self):
        return self.size
    
    def __str__(self):
        string = '['
        current = self.first
        for i in range(len(self)):
            string += str(current)
            if i != len(self) -1:
                string += str(', ')
            current = current.next
        string += ']'
        return string
'''
Nota: puede agregar mas metodos a los nodos como lo es
agregar desde el indice, borrar desde el final de un nodo,
buscar un nodo en la coleccion, entre otros como lo son operaciones
'''

mylist = LinkedList()

mylist.append(2)
mylist.append(3)
mylist.append(8)
mylist.append(5)
print(mylist)
mylist.delete(8)
print(mylist)