#POO
'''
Clase: Es una plantilla o modelo para crear a partir de ella
ciertos objetos. Esta plantilla es la que contiene la informacion,
caracteristicas y capacidades que tendra el objeto que sea creado a
partir de ella 
'''

'''
Tipos de  datos abstracto: En python todo es un objeto y tiene un tipo.
* Representacion de datos y la forme en la que interactuamos con ellos
* La forma de interatuar con ellos nos permite -Crear -Manipulacion -Destruccion
'''

'''
Ventajas de tener diferentes objetos en python:
* Decomposicion: Estructurar en objetos mas pequeños
Ejemplo: en un restaurante tenemos sillas, mesas, platillos, etc
* Abstraccion: No nos preocupamos por la forma en que se genera ese objeto
Ejemplo: Cuando pedimos una hamburguesa en el restaurante
no nos preocupa como la hicieron, que aceite usaron etc
* Encapsulamiento: Esconder datos que no consideramos importantes
para las personas que estan usando nuestras clases
'''

# Como definimos la clase:

'''
class <nombre_de_la_clase>(<super_clase>):
nota: algunas veces podemos poner una super_clase
como es en caso de la herencia
    def __init__(constructor)(self, <params>):
        <expresion>

    def <nombre_del_motodo>(self, <params>):
        <expresion>
self: es una referencia a esa misma clase
'''
#Ejemplo

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return print(f'Hola {otra_persona.nombre}, me llamo {self.nombre}')
    
#Como lo podemos usar
david = Persona('David', 35)
Carla = Persona('Carla', 40)

david.saluda(Carla)

#Instancia
'''
imaginemos que la clase es un molde, y el objeto creado 
creado de ese ocjeto es lo que conocemos como instancia

Importante: todos los metodos de una clase reciben
implicitamente como primer parametro el self
'''

#ejemplo

class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x) ** 2
        y_diff = (self.y - otra_coordenada.y) ** 2
        return (x_diff + y_diff) ** 0.5
    
if __name__ == '__main__':
    coord1 = Coordenada(3, 30)
    coord2 = Coordenada(4, 8)

    print(coord1.distancia(coord2))
    print(isinstance(coord1,Coordenada))

'''decomposicion: A partir de un problema mas grande , podemos
convertirlo en problemas mas pequeños en su lugar y facil de resolver
'''

#Ejemplo

class Automovil:
    def __init__(self, modelo, marca, auto, velocidad):
        self.modelo = modelo
        self.marca = marca
        self.auto = auto
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)
        self.velocidad = velocidad
        self.llantas =  Llantas(tipo='carreras', tamaño=16)
        #None significa que no tiene un valor asignado
        #Nota: el self._ significa que estamos asignando una variable privada
    def acelerar(self, tipo = 'despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(2)
        self._estado = 'en movimiento'

    def tipo_carro(self, velocidad):
        if velocidad == 200:
            self.auto('carreas')
        else:
            self.auto('uso diario')


class Motor:
    def __init__(self, cilindros, tipo = 'gasolina'):
        #El tipo = 'gasolina' es una variable por defecto que asignamos nosotros y
        #eso significa que podemos especificarlo directtamente o no
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina (self, cantidad):
        pass

class Llantas:
    def __init__(self, tipo, tamaño):
        self.tipo = tipo
        self.tamaño = tamaño
        self._material = 'plastico'