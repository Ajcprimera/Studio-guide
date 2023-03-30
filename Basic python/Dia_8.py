#conjuntos
'''
Los conjuntos son una cantidad de elementos agrupados que tienen
algo en comun, ademas los conjuntos cumplen con ciertas propiedades:
se pueden modificar
no tienen un orden en especifico
no permiten elementos duplicados
pueden ser de varios tipos
'''

set_countries = {'Colombia','Colombia', 'Bolivia'}
#Nota: si colocamos un elemento duplicado dentro del conjunto, el conjunto mismo
#lo va a eliminar
print (set_countries)

set_numbers = {1,2, 24, 64}
print (set_numbers)

#Podemos definir conjuntos mediante otras estructuras de datos
set_from_string = set ('hola')
#Aqui parte cada uno de los caracteres y los convierte en un elemento
#del conjunto
print (set_from_string)

#Tambien podemos tener un conjunto mediante una tupla o una lista
set_from_tuple = set(('abc', 'as', 'def'))
print(set_from_tuple)


set_from_list = set([145, 58, 74, 85])
print(set_from_list)

convert_list = list (set_from_list)
print(convert_list)

#Modificacion de conjuntos

size = len(set_countries) #para saber la cantidad de elementos del conjunto
print (size)

print('Colombia' in set_countries)
print('Peru' in set_countries)#Para saber si un elementos esta dentro de un conjunto

#Agregar elementos al conjunto (.add())
set_countries.add('Peru')
print(set_countries)

#Actualizar elementos (.update())

set_countries.update({'Mexico', 'Ecuador', 'Argentina'})
'''
La diferencia entre .add() y .update() es que .add solo permite
agregar elementos uno por uno y .update permite agregar un conjunto
de elementos
'''
print(set_countries)

#Para eliminar un elementodel conjunto (.remove()), ademas de lanzar un error si no encuentra
#el elemento dentro del conjunto

set_countries.remove('Colombia')
print(set_countries)

set_countries.discard('Argentina')
#el .discard() permite eliminar un elemento y si no existe no lanza ningún error.
print(set_countries)

set_countries.pop()
#El .pop() nos devuelve un elemento aleatorio y 
#lo elimina y si el conjunto está vacío lanza el error “key error”
print(set_countries)

#Limpiar todo el conjunto .clear()
set_countries.clear()
print(set_countries)

#Operaciones con conjuntos

#Union de conjuntos

set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#Con este metodo unir 2 conjuntos, respetando las reglas de los conjuntos
set_c = set_a.union(set_b)
print(set_c)

#Otro metodo para unir conjuntos (Mediante opradores matematicos)

print (set_a | set_b)#Lo unico que la diferencia es la sintaxis

#Intercesion de conjuntos.

#Con el metodo intersion nos permite saber un elemento en comun de
#los conjuntos
set_c = set_a.intersection(set_b)
print(set_c)

#Mediante operadores matematicos

print(set_a & set_b)

#Diferencia entre conjuntos

#Con el metodo diferencia nos permite realizar como una sustraccion de conjuntos,
set_c = set_a.difference(set_b)
print(set_c)

#Mediante operadores matematicos
print(set_a - set_b)

#Diferencia simetrica de  conjuntos

#Nos permite saber hacer una union de conjuntos, descartando los elementos
#en comun

set_c = set_a.symmetric_difference(set_b)

#Mediante operadores matematicos
print(set_a ^ set_b)