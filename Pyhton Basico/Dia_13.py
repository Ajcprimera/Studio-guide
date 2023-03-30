from Package_Dia_13.mod_1 import func_1, func_2
#Aqui el paquete no se inicializa 2 veces, sino 1
from Package_Dia_13.mod_2 import func_3, func_4
'''
Aqui estamos llamando la carpeta llamada Package_Dia_13 y de alli estamos llamamos al archivo mod_1,
despues importamos las funciones que vamos a usar dentro del archivo
'''

print(func_1())
print(func_2())
print(func_3())
print(func_4())

#caso para llamar __init__.py

import Package_Dia_13

print(Package_Dia_13.URL) #La url hace parte del paquete
print(Package_Dia_13.mod_1.func_1())#Tambien es posible llamar asi la funcion, 
#sin embargo este metodo es muy debil

#Iterables

#La funcion iter nos permite iterar manualmente una funcion
my_iter = iter(range(1, 11))
print(next(my_iter))#El next nos ayuda a iterar el rango de manera manera manual uno a uno

#Nota: hay que saber hasta donde debemos iterar, ya que, al llegar al limite de la iteracion
#Va a lanzar una ntificacion de llegada al limite

#Errores en python

#Creacion de errores propios

age = 20
if age < 18:
    raise Exception ('No se permiten menores de edad')#Raise nos permite hacer las excepciones de errores que nosotros vamos haciendo
    #Nota: cuando hacemos  un error y el error se da, el programa se detiene y deja de trabajar

#Algunos errores que muestra python mediante la terminal

'''
* ArithmeticError: Se genera cuando se produce un error en los cálculos numéricos
* AssertionError: Se genera cuando falla una declaración de afirmación
* AttributeError: Se genera cuando falla la asignación o la referencia de atributo
* Exception: Clase base para todas las excepciones
Si deseas ver mas de errores que muestra python, puede visitar:
https://www.w3schools.com/python/python_ref_exceptions.asp
'''

#Manejo de excepciones

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1!=1, 'Uno no es igual a uno'
except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        raise Exception ('No se permiten menores de edad')
except Exception as error:
    print(error)
'''
la funcion assert te permite probar si la condicion en retorna un 
True, si no lo hace, el programa muestra un AssertionError.
'''

try:
    print(0/0)
    assert 1!=1, 'Uno no es igual a uno'
    age = 20
    if age < 18:
        raise Exception ('No se permiten menores de edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)
#Try con varios exceptions