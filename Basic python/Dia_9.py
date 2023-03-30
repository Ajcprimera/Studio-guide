#List comprehension

#List comprehension ofrece un acorta sintaxis cuado tu quieres 
#crear una nueva lista basandose en los valores de una lista exixtente


n_1 = []
for i in range (1, 11):
    n_1.append(i*2)

print(n_1)

#Otro metodo para hacer list Comprehesion

n_2 = [i *2 for i in range (1, 11)]
print(n_2)
#Con cada elemento iterable, vamos a ir agreganedo elementos a la lista

n_3 = []
#Metodo normal, sin list comprehension
for i in range (1, 11):
    if i % 2 == 0:
        n_3.append(i*2)

print(n_3)

#Mediante list comprehension
n_4 = [i *2 for i in range (1, 11) if i % 2 == 0]
print(n_4)

#Dictionary comprehension

dict_1 = {}

for i in range (1,6):
    dict_1[i] = i * 2
    #Aqui incluimos la llaves al diccionario

print(dict_1)

#mediante dictionary comprehension
dict_2 = {i : i * 2 for i in range (1,6)}
print(dict_2)

#Partir la inicializacion de un diccionario mediante una lista
countries = ['col', 'mex', 'bol', 'pe']
population = {}
import random
for i in countries:
    population[i] = random.randint(1,100)

print(population)

population_2 = {i : random.randint(1, 100) for i in countries}

print(population_2)

#Iterando 2 lista, logrando generar un diccionario
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

#Metodo para uni las lista, generando una listas con tuplas
print(list(zip(names, ages)))

new_dict = {name : age for (name, age) in zip (names, ages)}
#primero generamos el par clave valor que desoues vienen de iterar una lista con tuplas

print(new_dict)

#Dictionary comprehension con condicinales

c_1 = ['col', 'mex', 'bol', 'pe']
population_3 = {}
population_3 = {i : random.randint(1, 100) for i in c_1}

print(population_3)

result = {coun : popu for (coun, popu) in population_3.items() if popu > 20}
#El .items() es para establecer la condicion solamente en los items del diccionario
print(result)

txt =  'Hola, soy Nicolas'
unique = {word : word.upper() for word in txt if word in 'aeiou'}
print(unique)

#Si desea saber cual usar de los co0njuntos utilizar dependiendo de su objetivo,
#Visualice la imagen de set-tuplas-listas
