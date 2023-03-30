#Estructura de datos lineales

#Arrays

'''
Conceptos claves que ya debemos haber comprendido:

* Elemento: valor almacendo en las posiciones del array

* Indice: referencia a la posicion del elemento
(desde 0 hasta n)
'''

#Nota: los array son diferentes de las listas, ya que 
#con los arrays nos permiten hacer ciertas restricciones

#Como podemos crear nuestro propio array

import random
import functools

class Array:
    def __init__(self, capacity, fill_value= None):
        self.items = list()
        
        for i in range (capacity):
            fill_value = random.randint(0, 100)
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __getitem__ (self, index):
        return self.items[index]

    def __setitem__ (self, index, new_item):
        self.items[index] = new_item
    
    def __sum__ (self):
        return functools.reduce(lambda a, b: a + b, self.items)
    
if __name__ == '__main__':
    elements = 5 #int(input('Ingrese la cantida de elememtnos del array: '))

    array = Array(elements)

    print(array.__str__())
    print(array.__sum__())

#Arrays con 2 dimensiones:

class grid():
    def __init__(self, columns, rows, fill_values = None):
        self.data = Array(rows)
        for i in range(rows):
            self.data[i] = Array(columns, fill_values)

    def get_height (self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"
        return str(result)
    
if __name__ == '__main__':
    matriz = grid(3,3)

    print(matriz)