#Pilas
'''
Que son: Es una estructura en la cual tenemos una coleccion
de datos y nos permite hacer hacer lo sgte:
- Añadir un elemento al final de la pila
- Sacar el ultimo elemento de la pila

Las pilas son estructuras relativamente comunes en el varias
areas de la computacion, en especial si queremos evaluar
expresiones, recursion, scope, etc
'''

class Stack:
    def __init__(self):
        self.top = None
        self.stack = []

    def gettoop(self):
        return self.top
    
    '''El metodo add nos ayuda el elemento
    Lo que hace este metodo es almacenar los datos
    en el tope de la coleccion, cumpliendo de esa manera
    '''
    def add(self, data):
        self.top = data
        self.stack.append(data)
        return self.top
    
    def __str__(self) -> str:
        return str(self.stack)
    
    def pop(self):
        self.stack.pop()
        self.top = self.stack[-1]

    def __len__(self):
        return len(self.stack)
    
stack = Stack()

stack.add(2)
stack.add(4)
stack.add(26)
stack.add(5)

print(stack)
print(stack.__len__())

stack.pop()
print(stack)
print(stack.__len__())

#Colas
'''
Que son: Son estructuras de datos de datos lineal
parecida a la pilas, sin embargo, esta respecta unas
condiciones diferentes a esta la cual es

- El primer dato introducido en la coleccion, va a ser el
primera en salir, es parecido a una cola en la vida real
'''

class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.queue = []

    def getStart (self):
        return self.start
    
    def getEnd (self):
        return self.end
    
    def add (self, data):
        if len(self.queue) == 0:
            self.initial = data
            self.final = data
            self.queue.append(data)
        elif len(self.queue) > 0:
            self.final = data
            self.queue.append(data)
            return self.final
    
    def pop (self):
        self.queue.pop(0)
        self.start = self.queue[0]
        return self.start
    
    def __str__(self) -> str:
        return str(self.queue)

    def __len__(self):
        return len(self.queue)
    

queue = Queue()
queue.add(10)
queue.add(12)
queue.add(7)
queue.add(5)

print(queue)
print(queue.__len__())

queue.pop()

print(queue)
print(queue.__len__())

#Cola basada en 2 pilas

class stackqueue:
    def __init__(self) -> None:
        self.inside_stack = []
        self.outside_stack = []

    def add (self, data):
        self.inside_stack.append(data)

    def remove(self):
        while self.inside_stack:
            self.outside_stack.append(self.inside_stack.pop())
        
        return self.outside_stack.pop(0) if self.outside_stack else None
        #Aqui estamos diciendo que si hay elementos en outside_stack, este los va
        #a eliminar, sino tiene elementos, este va a retornar None, indicando que
        #no hay datos en la cola

    def __str__(self) -> str:
        if self.inside_stack == []:
            return str(self.outside_stack)
        else:
            return str(self.inside_stack)

mystackqueue = stackqueue()

mystackqueue.add(5)
mystackqueue.add(7)
mystackqueue.add(9)
mystackqueue.add(25)
print(mystackqueue)

mystackqueue.remove()

print(mystackqueue)

#Colas con nodos

class twowaynode:
    def __init__(self, data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

class nodequeue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, data):
        node = twowaynode(data, None, None)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

        self.count += 1

    def remove(self):
        current = self.head

        if self.count == 1:
            self.count -=1
            self.head = None
            self.tail = None

        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -=1

        return current.data
    
my_node_queue = nodequeue()
my_node_queue.add(5)
my_node_queue.add(3)
my_node_queue.add(4)
my_node_queue.add(8)

print(my_node_queue.head.data)
print(my_node_queue.head.next.data)
print(my_node_queue.tail.data)

print(my_node_queue.remove())