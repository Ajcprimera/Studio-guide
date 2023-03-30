#Bucles while
counter = 0

'''
while counter < 10:
    counter += 1
    print (counter)
'''


'''
Los bucles whiles son bucles que se pueden ejecutar
de manera infinita mientra se cumpla la ejecucion establecida
por el usuario, no obstante, nosotros podemnos bucle estableciendo
condicines especificas para que se detenga
'''
'''
while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter)
'''

'''
La funcion break es una funcion forzada para romper un ciclo
'''
while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)

'''
La funcion continue nos permite establecer una condicion de que mientras el
counter sea menor a 15 la condicion del print no se ejecuta, sino hasta que llegue a 15
la condicion del print empieza a ejecutarse
'''
print ('*' * 10, '\n')

# ciclo for
for i in range (1,21):
    print(i)

print ('*' * 10, '\n')
'''
el ciclo for nos permite ejecutar mediante unas codiciones especificas
dentro de un rango dado establecido por el usuario y sin la necesidad hacer
operaciones extras
'''

my_list = [23, 45, 89, 67, 43]
for i in my_list:
    print (i)

print ('*' * 10, '\n')

'''
aqui estamos haciendo un ciclo para recorrer e iterar la lista
'''

my_tuple = ('nico', 'jule','santi')
for i in my_tuple:
    print (i)

print ('*' * 10, '\n')

product = {
    'name': 'camisa',
    'price': 100,
    'stock': 89
}

for i in product:
    print (product[i])

# un metodo para saber los valores dentro de las llaves

for key, value in product.items():
    print (key, ': ', value)

people = [
    {
        'name':'nico',
        'age' : 34
    },
    {
        'name':'zule',
        'age': 45
    },
    {
        'name':'santi',
        'age' : 4
    }
]#Lista de diccionarios

for person in people:
    print(person['name'])