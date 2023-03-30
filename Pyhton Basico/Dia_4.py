#Condicionales
if True: #Los if siempre se operan bajo condiciones booleanas
    print ('deberia ejecutarse')

if False:
    print('Nunca debe ejecutarse')

#Ejemplo

pet = input('Cual es tu mascota favorita: ')

#Caso 1 (Condicionales simples)
if (pet == 'perro'):
    print('Genial tienes buen gusto')
if pet == 'gato':
    print('espero tengas suerte')

'''
Nota: los parametros  que uno quiera que cumpla la condicion 
se peden poner tanto en parentesis como sin ellos
'''

#Caso 2 (Condicionales complejos)

Stock = input('Ingrese un numero stock: ')
Stock = int(Stock)
if Stock >= 100 and Stock <= 1000:
    print('El stock es correcto')
else:
    print('El stock es incorrecto')

#Caso 3 (Condicionales multiples)

pet = input('Cual es tu mascota favorita: ')

if pet == 'perro':
    print('Genial tienes buen gusto')
elif pet == 'gato':
    print('espero tengas suerte')
elif pet == 'pez':
    print('Eres lo maximo')
else:
    print('No tienes una mascota interesante')

#Ejemplo

n = int(input('Ingrese un numero: '))
if n % 2 == 0:
    print('Es un numero par')
else:
    print('No es un numero par')

#String Recargados

#Operador in
txt = 'Ella sabe programar en Python'
print('JavaScript' in txt)
print('Pythonn' in txt)

'''
El Operador IN nos permiter saber si un caracter
esta dentro de una variable
'''

#Ejemplo con condicionales

if 'Python' in txt:
    print('Elegistes bien')
else:
    print('Tambien elegistes bien')

#Operador len

size = len('empatia')
print(size)

size_2 = len(txt)
print(size_2)

'''
El operador LEN nos permite saber el tamaño o cantidad de caracteres 
que tiene una variable (en el caso de str tambien 
cuentan los espacios como un caracter)
'''

#Intruccion upper

print(txt.upper())

'''
La instruccion upper permite poner a todos los caracteres tipo string en mayusculas
'''
print(txt.lower())


'''
La instruccion lower permite poner a todos los caracteres tipo string en minusculas
'''

print(txt.count('a'))
'''
La instruccion count permite contar el numero de apariciones que tiene una letra
'''

print(txt.swapcase())
'''
La instruccion swapcase permite poner a todos los caracteres tipo string 
que estan en mayusculas a minuculas y viceversa
'''

print(txt.startswith('Ella'))
'''
La instruccion startswith permite saber si un texto
inicia con algo en especifico y nos va a arrojar un
valor booleano
'''

print(txt.endswith('Rust'))
'''
La instruccion endswith permite saber si un texto
termina con algo en especifico y nos va a arrojar un
valor booleano
'''

print(txt.replace('Python', 'Go'))

'''
La instruccion replace nos permite reemplazar una palabra del del texto
por otro
'''

txt_2 = 'este es un titulo'
print(txt_2)

print(txt_2.capitalize())

'''
La instruccion capitalize nos permite poner el primer caracterer en mayusculas
'''

print(txt_2.title())
'''
La instruccion title nos permite poner en el inicio de cada una de las palabras en mayusculas
'''

print(txt_2.isdigit())
'''
La instruccion isdigit nos permite saber si un
texto es un digito o un potencial digito
'''