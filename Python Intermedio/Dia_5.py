#Busquedad lineal

'''
Es un algoritmo empieza a buscar desde una lista empezando por el primer 
elemento de la lista, y continua hasta conseguir el elemento
de la lista
'''
#ejemplo
import random
def busquedad_lineal(lista, objetivo):
    match = False
    
    for i in lista:#ciclo que recorre la lista para verificar el elemento
        if i == objetivo:
            match = True
            break

    return match

if __name__ == '__main__':
    tama_lista = int(input('Tamaño: '))#tamaño de la lista
    objetivo = int(input('Ingrese objetivo: '))#numero objetivo

    lista = [random.randint(0, 100) for i in range (tama_lista)]#generamos lista
    respuesta = busquedad_lineal(lista, objetivo)#llamamos a la funcion
    print(lista)
    print(f'El elemento {objetivo} {"esta" if respuesta else "no esta"} en la lista')


#Busqueda binaria

'''
Este algoritmo toma una estrategia llamada divide y conquista, y recibe
el nombre de busqueda binaria ya que se divide en 2 cada iteracion, el 
principal problema que al usarlo, la lista debe estar ordenada
'''

def busquedad_binaria(lista, start, end, objetivo):
    print(f'buscando {objetivo} entre {lista[start]} y {lista[end-1]}')
    
    if start > end:
        return False
    
    middle = (start - end) // 2

    if lista[middle] == objetivo:
        return True
    elif lista[middle] < objetivo:
        return busquedad_binaria(lista, middle + 1, end, objetivo)
    else:
        busquedad_binaria(lista, start, middle-1, objetivo)



if __name__ == '__main__':
    tama_lista = int(input('Tamaño: '))#tamaño de la lista
    objetivo = int(input('Ingrese objetivo: '))#numero objetivo

    lista = sorted([random.randint(0, 100) for i in range (tama_lista)])#generamos lista ordenada
    respuesta = busquedad_binaria(lista,0 , len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if respuesta else "no esta"} en la lista')

#Ordenamiento de burbuja
'''
Es un algoritmo que recorre repetidamente una lista que necesita ordenarse. 
Compara elementos adyacentes y los intercambia si están en el orden incorrecto.
'''

def ordenamiento_de_burubuja(lista):
    
    n = len(lista)

    for i in range (n):
        for j in range (0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

if __name__ == '__main__':
    tama_lista = int(input('Tamaño: '))#tamaño de la lista
    
    lista = [random.randint(0, 100) for i in range (tama_lista)]#generamos lista
    print(lista)
    respuesta = ordenamiento_de_burubuja(lista)
    print(respuesta)

#Insertion sort
'''
Este algoritmo ordena "en su lugar", eso quiere decir que no
es necesario de memoria adicional ya que solo modifica los valores
de memoria

Como funciona:

* El primer elemento esta ordenado por definicion y los 
elementos se empezaran a ordenar a partir de este primer
elemento

* Se empieza a recorrer el resto de los elementos de la lista
y comparandolos, si uno de los elementos es mayor, se empieza
a mover uno a derecha y se inserta un nuevo elemento

* Se repite el paso anterior con todos los elementos de la
lista hasta tenerla ya ordenada

Visitar la sgte pagina para ver a mas detalle: https://visualgo.net/es/sorting
'''

def ordenamiento_por_insercion(lista):

    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion_actual = i

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        lista[posicion_actual] = valor_actual
    return lista

if __name__ == '__main__':
    tama_lista = int(input('Tamaño: '))#tamaño de la lista
    
    lista = [random.randint(0, 100) for i in range (tama_lista)]#generamos lista
    print(lista)
    respuesta = ordenamiento_por_insercion(lista)
    print(respuesta)

#Ordenamiento por mezcla
'''
Este tipo ordenamiento consiste en dividir una lista en listas
mas pequeña y mas pequeña, dejando lista de un solo elemento
y despues ir comparando los elementos de la listas e irlos recombinando,
logrando formar la lista ordenada


Ver el sgte video si quiere de manera grafica el funcionamiento del algoritmo:
https://www.youtube.com/watch?v=XaqR3G_NVoo
'''

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        middle = len(lista) // 2
        #aqui dividimos la lista en 2
        left = lista[:middle]
        right = lista[middle:]

        ordenamiento_por_mezcla(left)
        ordenamiento_por_mezcla(right)
        #aplicamos recursividad

        i, j, k = 0, 0, 0

        while i < len(left) and j< len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i+=1
            else:
                lista[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            lista[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            lista[k] = right[j]
            j+=1
            k+=1
    return lista

if __name__ == '__main__':
    tama_lista = int(input('Tamaño: '))#tamaño de la lista
    
    lista = [random.randint(0, 100) for i in range (tama_lista)]#generamos lista
    print(lista)
    respuesta = ordenamiento_por_mezcla(lista)
    print(respuesta)