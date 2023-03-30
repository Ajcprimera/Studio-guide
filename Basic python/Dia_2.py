#Tema de Operadores

#Operadres aritmeticos simples

from calendar import c


print(8 + 7) #Operador de suma
print(10 - 9) #Operador de resta
print(8 * 7) #Operador de multiplicacion
print(12 / 6) #Operador de division
print(54 % 5) #La operacion de modulo nos permite conocer el resto de una division
print(12 // 6) #Operador de division de manera entera
print(8 ** 7) #Operador de potencia

#Nota se pueden mezclar varios operadores

'''
Nota: algunos operadores se pueden utilizar para cadenas de texto
Sin embargo si queremos mezclar cadenas de texto con numeros debemos convertirlo
'''

print("Hola" + " Mundo")
print("Hola" + str (6))
print("Hola " * (2**3)) #Caso especial

#Operadores de comparacion

print( 5 > 6) #Mayor que
print( 5 < 6) #Menor que
print( 5 >= 6) #Mayor igual que
print( 5 <= 6) #Menor igual que
print( 5 == 6) #Igual que
print( 5 != 6) #Diferente de

#Operadores de Asignacion

x = 10
x += 3
print(x) #Operador para suma para la misma variable

y = 10
y -= 3
print(y) #Operador para resta para la misma variable

z = 10
z *= 3
print(z) #Operador para multiplicacion para la misma variable

w = 10
w /= 3
print(w) #Operador para division para la misma variable

h = 10
h %= 3
print(h) #Operador para modulo para la misma variable

g = 10
g //= 3
print(g) #Operador para division entera para la misma variable

i = 10
i **= 3
print(i) #Operador para potenciacion para la misma variable

#Operadore Logicos

print (3 > 4 and "Hola" > "Python")
print (3 > 4 or "Hola" > "Python")
print (not(3 > 4)) #Para negar la condicion

#Nota: Aprenderse las tabla de verdad