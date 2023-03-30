#Filter
n = [1,2,3,4]
new_n = list(filter(lambda x: x % 2 == 0, n))#Dentro de la funcion establecemos la condicion y el filter
#comienza a iterar la lista, creando una nueva lista
print(new_n)
#filter con diccionarios
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

wins = list(filter(lambda w: w['home_team_result'] == 'Win', matches))
#Aqui estamos filtrando los equipos que ganaron
print(wins)

#Reduce

import functools

numbers = [1,2,3,4]
result = functools.reduce(lambda a, b: a + b, numbers)
#La funcion reduce nos permite una lista a un valor unico, como si fuera una conclusion
print(result)

def accum(counter, item):
    return counter + item

result = functools.reduce(accum, numbers)#(funcion, la lista que queremos iterar)

#Modulos
import sys #Nos permite saber en sistema estamos trabajando
print(sys.path)#para saber la ruta del archivo con el cual estamos trabajando

import re #Para expresiones regulares
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57'
result_v2 = re.findall('[0-9]+', text)
print(result_v2)

import time #Nos ayuda saber al hora o fecha

timestamp = time.time()
print(timestamp)
local = time.localtime()
result_v3 = time.asctime(local)#Para dar el fomato de la hora
print(result_v3)

import collections #Para manejar listas

x = [1,2,3,4,3,2,3,1,3,4,7,9]
counter = collections.Counter(x) #para saber la frecuencia de un elemento
print(counter)

#Creacion de modulos propios
import utils #Una libreria que creamos nosotros mismo con varias funciones
data = [
    {'Country': 'Colombia',
    'Population': 300},
    {'Country': 'Bolivia',
    'Population': 400}
]
country = input('Ingrese un pais: ')
result = utils.population_by_country(country, data)

#Dualidad de archivos

#Si desea saber como funciona la dualidad de archivos, visite main_Dia_12
