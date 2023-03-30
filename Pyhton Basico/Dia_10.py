#funciones

#Las funciones nos permiten gran reutilizacion de codigo, ademas permitirnos 
#usarlas varias veces con diferentes parametros

def my_print():
    print('This is my print')
    print('This is my print 2')

my_print() #Podemos empezar a usar la funcion llamandola y al ser llamada,
#va a ejecutar los bloques de codigo dentro de la funcion

def my_print_2 (text):
    print(text * 2)

my_print_2('Esto es my texto')
my_print_2('Hola')#Como se muestra, se puede reutilizar la funcion y cambiar los
#valores del parametro

def suma(a, b):
    print(a + b)

def suma_2(c, d): #Podemos reutilizar una funcion dentro de otra
    my_print_2 (c + d)#Como el parametro no esta  definido puede recibir cualquier valor
    #por lo cual empieza a multiplicar los enteros

'''
Nota: El valor que ingresas cuando llamas la funcion se llama PARAMETRO (lo que esta dento de los 
parentesis de la funcion), Mientras que el valor que usamos dentro de la funcion se llama ARGUMENTO
(los valores que colocamos cuando llamamos la funcion)
'''

suma(1, 5)
suma(10, 5)
suma_2(2, 8)

#Funciones: return

def sum_with_range (min, max):
    sum = 0
    for i in range (min, max):
        sum += i #Aqui estamos sumando los valores dentro del rango recorrido
    return sum #Aqui estamos retornando el resultado del calculo final

ans = sum_with_range(1, 10) #Al ya retornar el valor, lo podemos asignar a una variable
print(ans)

ans_2 = sum_with_range(ans, ans + 10) #Aqui estamos poniendo el ans como parametro de entrada
print(ans_2)

#Parámetros por defecto y múltiples returns

def find_volume (length, width, depth): #Metodo para hacer retorno de multiples parametros,
    #podemos hacer un retorno de los parametros de diferentes forma (Operaciones o solo retornando cada una)
    return length * width * depth

def find_volume_2 (length_2 = 1, width_2 = 2, depth_2 = 1): #Aqui estamos poniendo los valores de manera direscta
    #en los parametros, aun que despues la podemos ir cambiando dependiendo de los valores que le pongamos
    #cuando es llamada
    return length_2 * width_2 * depth_2

def find_volume_3 (length, width, depth): 
    return length * width * depth, width, 'hola' #Tmabien podemos retornar valores obtenidos fuera de los parametros
result = find_volume(4, 5, 8)
result_2 = find_volume_2 ()
result_3 = find_volume_2 (4, 5, 8)
result_4, width, string = find_volume_3 () #Asignamos una variable para cada uno de los valores retornados
result_5 = find_volume_3 ()

print(result)
print(result_2)
print(result_3)
print(result_5) #Aqui nos los retorna en forma de tupla 

print(result_4)
print(width)
print(string)

#El scope
'''
Dentro de una función puede haber variables, las cuales se llaman variables locales. Estas variables locales, 
se identifican porque están escritas dentro de la definición de la función; y únicamente funcionan mientras que la 
función sea llamada o utilizada. Si vas a llamar a una variable local por fuera de la función, no servirá.
Y existen variables globales, que son las que están escritas fuera de una función. Estas variables si funcionan al ser 
llamadas sin la función, porque no están determinadas dentro de la función.
'''

price = 100 #Alcance global, ya que tiene un alcance dentro de todo el archivo

def increment():
    price = 200
    price = price + 10 #Aqui se esta definiendo una variable y solo tiene un contexto dentro de la 
    #funcion (Variable local)
    print(price)
    return price

def increment_2():
    price = 200
    result = price + 10 #tiene un contexto dentro de la funcion y solo va a funcionar de esa funcion
    print(result)
    return result

print(price)
price_2 = increment()
print(price_2)