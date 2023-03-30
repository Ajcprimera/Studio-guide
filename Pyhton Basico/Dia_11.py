#Lamdba
def increment(x):
    return x + 1

result = increment(10)
print(result)

#Pasar una funcion a lambda

#Una funcion lambda es aquella que pueda tomar un numeros de argumentos, pero que puede tener una sola expresion
increment_v2 = lambda x : x + 1

result_v2 = increment_v2(20)
print(result_v2)

#Cuando recibimos 2 valores
x = lambda a, b : a * b
print(x(5, 6))

#Caso tipo string
full_name = lambda name, last_name : f'Full name is {name} {last_name}'
'''
f" Lo que hace que sea posible interpolar código encerrando este en llaves {} dentro de la cadena. 
Obteniendo como resultado una cadena de texto.
'''
fullname = full_name('Alex', 'Perez')

'''
La mejor forma de darle el mejor uso a la funcion lambda es usandolas como funciones anonimas
de de otras funciones
'''

#Ejemplo
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#Higher order function: una función dentro de otra función

def increment_v3(x):
    return x+1

def high_ord_func (x, func):#Como se puede ver, aqui la funcion esta recibiendo tambien otro 
    #paramentro como funcion
    return x + func(x)# y al ejecutar esta funcion tambien debemos enviarle un parametro de entrada

result_v3 = high_ord_func(2, increment_v3)#Aqui solo estamos enviando al funcion

print(result_v3)

increment_v4 = lambda x: x+1
high_ord_func_v2 = lambda x, func : x+func(x)

print(high_ord_func_v2(2,increment_v4))

result_v5 = high_ord_func_v2(2, lambda x: x + 3)
print(result_v5)

'''
Nota Importante:
Normalmente solemos usar parámetros y argumentos como sinónimos, 
y en la práctica podemos inferir lo que esto significa según el contexto. 
Pero en un entorno profesional, deberíamos tener muy claro que los parámetro 
son las reglas o instrucciones que definimos dentro de la función, mientras los 
argumentos son los datos que le pasamos a la función para que los “reemplace” y ejecute la función.

Algo así como en matemáticas básicas, cuando definimos y = x^2 + x + 3, la derecha de la ecuación 
serían los parámetros, mientras que los argumentos, serían los valores que le asignamos a la x, 
bien sea para encontrar las coordenadas de un punto (una iteración), o para trazar
 la gráfica completa (multiples iteraciones)…

**Parámetros: **Reglas Internas de la Función.

**Argumentos: **Datos Externos que le Pasamos a la Función para que Pueda Hacer sus Cálculos.
'''

#Map

numbers = [1, 2, 3, 4]
answer = list(map(lambda i: i * 2, numbers))
print(answer)

numbers_v2 = [1,2,3,4]
numbers_v3 = [4,5,6]
answer_v2 = list(map(lambda g, h: g + h, numbers_v2,numbers_v3))#Aqui va a mostrar el resultado de la suma
#dependiendo de la lista menor

#Map con diccionarios
items = [
    {
        'products': 'camisa',
        'price':100
    },
    {
        'products': 'pantalones',
        'price':200
    },
    {
        'products': 'pantalones 2',
        'price':300}
]

prices = list(map(lambda a: a['price'] ,items)) #Manera de de iterar el mapeo de diccionarios
#Crea unua nueva lista y no modifica la original
print(prices)

def add_taxes(item):
    item['taxes'] = item['price'] * 0.19
    return item

new_items = list(map(add_taxes,items))
print(new_items)
print(items)#Lista modificada

'''
Nota:
hay que tener en cuenta que es lo que queremos hacer con el mapeo de diccionarios
ya que el map con la funcion lambda nos permite crear una nuava lista, sin embargo,
cuando queremos hacer funcones mas complejas debemos usar un def, este modifica la lista
de diccionarios
'''

#Metodo parta evitar que ocurra modificacion de la lista original
def add_taxesv2(itemv2):
    new_item = itemv2.copy()#Creamos practicamente una nueva lista copiando los valores de la lista original
    new_item['taxes'] = new_item['price'] * 0.19
    return new_item