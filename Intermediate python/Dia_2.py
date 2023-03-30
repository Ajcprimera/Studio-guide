#Abstraccion
'''
La abstraccion nos permite enfocar la informacion relevante 
del codigo, logrando separar la informacion central de los
detalles no tan relevantes, tambien podemos usar variables
publicas y privadas
'''

#ejemplo:

class Lavadora:
    def __init__(self):
        '''aqui estamos diciendo que no hay un cuerpo en esta 
        funcion y que simplemente la dejemos pasar'''
        pass
    def lavar (self, temperatura = 'caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()#Generamos variables privadas que no son 
        #relevantes para el usuario

#Base de los decoradores


'''funcion de orden superior: estas funciones son aquellas que toman
otra funcion como parametro o que retornan una funcion como resultado
ejemplo:
1)int foo(Funtion param): en este caso la funcion foo  toma la funcion
param y la utiliza para generar un valor entero
2)Funtion bar(int x): funcion bar que recibe un entero y genera una
funcion
3)Funtion bar(Funtion x): una funcion que reciba una funcion para
genera una funcion totalmente distinta

De esta forma un decorador añade capacidades a una 
función sin modificarla.
'''
#ejemplo
def presentarse(nombre):
	return print(f"Me llamo {nombre}")

def estudiemos_juntos(nombre):
	return print(f"¡Hey {nombre}, aprendamos Python!")

def consume_funciones(funcion_entrante):
	return funcion_entrante("David")

consume_funciones(presentarse)#llamamos la funcion que recibe como parametro otra funcion

#Funciones anidadas


def funcion_mayor():
	print("Esta es una función mayor y su mensaje de salida.")

	def librerias():
		print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

	def frameworks():
		print("Algunos frameworks de Python son: Django, Dash y Flask.")

	frameworks()#llamamos ambas funciones dentro de la funcion
	librerias()
	
funcion_mayor()

#getters y setters
'''
estos tiene el objetivo de encapsular datos
'''

#ejemplo sin getter y setter
class Millas:
	def __init__(self, distancia = 0):
		self.distancia = distancia#ejecutar

	def convertir_km (self):#ejecutar ()
		return self.distancia * 1.609344
	
avion = Millas()
avion.distancia = 200

print(avion.convertir_km())

#ejemplo con setter y getters

class Milla_2s:
	def __init__(self, distancia = 0):
		self.distancia = distancia

	def convertir_km (self):
		return self.distancia * 1.609344
	
	#metodo getter
	def definir_distancia(self):
		return self._distancia #creamos una variable privada
	
	#metodo setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		self._distancia = valor
#Explicacion del codigo:

'''
con el metodo getter nos permitira obtener el valor de la
distancia y el metedo getter nos permitira hacer la
restriccion, es importante enfatizar que la distancia fue
cambianda por _distancia, enfocando que es una variable privada
'''

#funcion property()
'''
Esta funcion nos ayuda a crear y retornar la propiedad de un objeto
la propiedad del objeto posee los sgtes metodos getter(), setter ()
y del()

Eso quiere decir que la funcion debe tener 4 atributos (fget, fset,
fdel(), fdoc)

* fget: trae el valor de un atributo
* fset: define el valor del atributo
* fdel: elimina el valor del atributo
* fdoc: crea un docstring por atributo
'''

#ejemplo:

class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia(getter)
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia(setter)
	def definir_distancia(self, recorrido):
		print("Llamada al método setter")
		self._distancia = recorrido

	# Función para eliminar el atributo _distancia(del)
	def eliminar_distancia(self):
		del self._distancia

	distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

print(avion.distancia)