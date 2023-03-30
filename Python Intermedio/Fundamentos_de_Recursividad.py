#Recursividad
'''
Que es: Es una tecnica  mediante la cual 
una  funcion se llama asi misma
'''

#Ejemplo
def factorial (n):
    if n == 0:
        return 0
    if n == 1:
        #Aqui si el valor ingresado es 1, me va a retornar el
        #mismo valor
        return 1
    #Aqui empezamos a iterar dentro de la misma funcion llamandola
    #otra vez
    return  n * factorial(n - 1)
'''
Nota: en el caso de factorial debemos colocar 2 return debido a que si no
retornamos el 0, este no mostrar el error de limite de recursividad

pueden intentarlo, quitando el condicional con el respectivo return de
la funcion
'''
def fibonacci(n):
    if n == 0 or n == 1:
        #Condicion base para la sucesion de fibonacci
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

'''
Nota: La recusividad tiene un limite de llamadas recursivas (1000)
'''

n = int(input('Ingrese un numero: '))

print(fibonacci(n))
print (factorial(n))