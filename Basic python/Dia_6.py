#Tuplas

#Las tuplas no es posible hacer cambios en ellas, ni declarar
# mas datos en ella y puede almacenar diferentas tipos de datos,
#por lo cual nos servira para datos de lectura
n = (1, 2, 3, 4)
s = ('nico', 'zule', 'santi', 'nico')

print('0 => ', n[0])#para saber la posicion de un elemento
print('-1 => ', n[-1])#para saber la ultima posicion de un elemento

print(s.index('zule'))#para saber en que posicion esta un elemento
print(s.index('nico'))#para saber cuantos elementos repetidos esta e la tuplas

'''
A pesar de que no podamos cambiar los elementos de la tupla, es posible tramformar
las tuplas a lista para poder trabajar con ellas
'''

#Ejemplo
m_l = list(s)
print(m_l)
print(type(m_l))

m_l[1] = 'lucy'
print(m_l)

#Tambien es posible hacerlo en vicerversa
m_t = tuple(m_l)
print(m_t)
print(type(m_t))

#Diccionarios

'''
Los Diccionarios son objetos los cuales se pueden ordenar,
cambiar y ademas no permite valores duplicados
'''
m_d = {
    'avion' : 'bla bla bla',
    'name' : 'nicolas',
    'Last_name' : 'Molina',
    'Age' : 75
}

print(m_d)
print(len(m_d))#Para saber cuantos elementos pares tenemos en el diccionario
print(m_d['Age'])#En estos casos nosotros podemos directamente en el elemento que nos interesa
#en vez de buscarlo por suy posicion
print(m_d['Last_name'])
print(m_d.get('valor'))
'''
La diferencia entre .get() y buscar el elemento con los corchetes, es que 
en el caso de que saber si un elemento esta en el diccionario o hayamos copiado
mal el elemento que hemos escrito, este va a ser capaz de trabajarlo y mostrarnos una
alerta(None), lo cual los corchetes no muestra y da error en el codigo
'''

print('avion' in m_d)#Para asegura si esta en el diccionario retornando un valor booleano (True, False)
print('kjsahdlakfgr' in m_d)

#Metodos para modificar el diccionario

person = {
    'name' : 'nicolas',
    'Last_name' : 'Molina',
    'Age' : 75,
    'Langs' : ['python', 'javascript']
}#Clave : Valor
print(person)

person['name'] = 'juan' #para cambiar el nombre dentro de name
person['Age'] -= 50 # Tambien podemos hacer ajustes sobre los valores actuales
#en este caso restar la edad
person['twitter'] = '@nicobytes' #Para agregar tambien nuevos valores al diccionario
person['Langs'].append('rust')#Agregar un elemento al diccionario
print(person)

del person ['Last_name']#Elimina los elementos almacenados dentro del diccionario
person.pop('Age') #Otro metodo para eliminar elementos dentro dl diccionario y debe recibir un argumento

print(person)

print(person.items())#Permite devolve los pares clave-valor en forma de tuplas
print(person.keys())#Permite devolver una lista con los atributos llaves del diccionario (No se fija los valores)
print(person.values())#Permite devolver una lista los valores llaves del diccionario