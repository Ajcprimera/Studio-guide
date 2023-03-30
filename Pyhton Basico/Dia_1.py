# Hola mundo
print ("Hola python") # el print lo usamos para imprimir en consola

# Tipos de comentarios
# Comentaios simples se usa el #

"""
Esto es un comentario 
en multiples lineas
"""

'''
Esto es un comentario 
en multiples lineas
pero con comilla simples
'''

#Manera de consultar el tipo de dato

print(type("hola mundo")) #Debe salir un dato tipo str
print(type(5)) #Debe salir un dato tipo int (para numeros enteros)
print(type(5.3)) #Debe salir un dato tipo float (para numeros decimales)
print(type(False)) #Debe salir un dato tipo booleano
print(type(3 + 1j)) #Debe salir un dato tipo complejo

#Tema de variables

#La forma de nombrar las variables siempre debe ser en minusculas en python
my_variable_str = "My string Variable"
"""
Forma correcta de escribir una variable (en minusculas y
si queremos 2 palabras usamos un backslash)
"""

"""
Nota: no siempre es correcto escribir variables demasiado largas
"""
print(my_variable_str)

#Formas que no correctas de escribir una variable:
'''
first-name Forma 1
first@name Forma 2
first$name Forma 3
num-1 Forma 4
1num Forma 5
'''

my_variable_int = 6
print (my_variable_int)

my_variable_bool = True
print (my_variable_bool)

#Forma de convertir las variables
my_variable_int_to_str = str(my_variable_str)
print(my_variable_int_to_str) #Nota si lo convertimos a un caracter tipo str ya no se puede usar para operaciones matematicas

#Maneras de imprimir variables
#Con comas

print(my_variable_str, my_variable_int, my_variable_bool)

#Con suma
print(my_variable_str + str(my_variable_int)) #En este caso debemos convertir al tipo de variable que queremos imprimir

#Otra forma de concatenar
print("este numero es ", my_variable_int)

#Para saber el tamaño de la variable
print(len(my_variable_str)) #Con la funcion len() podemos ver el tamaño de la variable

#Otra forma de declarar variables (Variables en una linea)
#Hay que tener cuidado ya que se puede cometer mcho error en la sintaxis del codigo

nombre, apellido, edad = "Albert", "Carruido", 19 #Se puede diferentes tipos de datos
print(nombre)

#Agregar datos de las variables por nosotros mismos
add_number = int(input("add a number: ")) #la funcion input nos permite agregar datos por nosotros mismos en la terminal
print(add_number)

#Nota: es posible cambiar los datos de la variables y su tipo