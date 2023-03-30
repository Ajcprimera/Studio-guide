#Trabajo con valores booleanos
is_single = True

print(type(is_single))

is_single = False

print(is_single)

'''
Nota: con el operardor not podemos cambiar los valores de los
booleanos
'''

print(not True)
print(not False)

#Caso 2
is_single = not is_single
print(is_single)

#Flotantes

x = 3.3
print(x)

y = 1.1 + 2.2

print(y)

print(x==y) #Va a dar un falso debido a la presicion decimal de Y

#Caso para reducir la presicion decimal

#Caso 1 (Convirtiendo la Y a un str)

y_format = format (y, ".2g") #El .2g es para limitart la cantidad de digitos de Y
print(y_format == str(x))

#Caso 2 (Limitar la cantidad decimal de forma matematica)
tolerance = 0.00001
print(abs(x - y) < tolerance) 
'''
En este caso se eta restando x e y para extraer 
la diferencia decimal y con el valor absoluto para que de positivo
ahora bien, esa resta nos va a dar una margen de error, la cual es
la diferencia de esa resta, y despues hacer una comparacion con la tolerance
para que nos de el true

'''

#Operadores logicos (parte 2)

print('AND') #El operador "AND" nos permite que si una de las condiciones no se cumplen, la condicion final va a dar un false

#CASO CON BOOLEANOS
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

#CASO CON NUMEROS
print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

#Ejemplo
Stock = input('Ingrese un numero stock: ')
Stock = int(Stock)

print(Stock >= 100 and Stock <= 1000)

print('OR') #El operador "OR" nos permite que, si algunas de las condiciones se cumplen, la condicion final nos debe dar true

#CASO CON BOOLEANOS
print('True and True =>', True or True)
print('True and False =>', True or False)
print('False and True =>', False or True)
print('False and False =>', False or False)

#Ejemplo

role = input('Digita el rol: ')
print(role == 'admin' or role == 'seller')

#Negador
'''
El operador "NOT" nos ayuda a negar lo que son variables tipos booleanas
cambiando el valor booleano
'''

print (not True)
print (not False)

print('True and True =>', not (True and True))
print('True and False =>', not (True and False))
print('False and True =>', not (False and True))
print('False and False =>', not (False and False))

Stock = input('Ingrese un numero stock: ')
Stock = int(Stock)

print(not (Stock >= 100 and Stock <= 1000)) 
'''
Aqui estamos negando la condicion boleeana, lo cual si la condicion se cumple, 
igualmente va a dar a false, ya que la estamos negando o viceversa
'''