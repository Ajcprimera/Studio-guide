#Leer archivos de texto

#como leer  el archivo
file = open('Pyhton Basico/text.txt')#Abrir desde la ruta de la carpeta en caso de que el archivo este almacenado en una
print(file.read())#Leer todo el archivo
print(file.readline())#Va a leer las linea del archivo uno por uno y en forma de lista

for i in file:
    print(i)#Una manera ligera de recorrer el archivo

file.close()#para cerrar el archivo

with open('Pyhton Basico/text.txt') as file: #otra forma cerrar el archivo de forma automatica de cerrar el archivo
    #una vez usado
    for i in file:
        print(i)

#Escribir en un archivo

'''
with open('Pyhton Basico/text_2.txt', 'w') as file_2:#Aqui habilitamos los permisos de escritura,
    #sin embargo, ya no tenemos los permisos de lectura
    for x in file_2:
        print(x)
    file.write('nuevas cosas en este archivo')
    
    * esto va a marcar un  error ya que esta solo en modo de escritura y no de lectura
    '''

with open('Pyhton Basico/text_2.txt', 'r+') as file_2:#Aqui estamos hablitando ambas funciones
    #(escritura y lectura)
    for y in file_2:
        print(y)
    file_2.write('nuevas cosas en este archivo')#leo y escribio en el archivo .txt
    file_2.write('nuevas cosas en este archivo\n')#Agregarlo con un salto de linea
    file_2.write('otra linea\n')

with open('Pyhton Basico/text_3.txt', 'w+') as file_3:#Aqui estamos habilitando ambas funciones
    #(escritura y lectura), ademas de sobre escribir todo lo que esta en el archivo y reemplazar por nuevas lineas
    for y in file_3:
        print(y)
    file_3.write('nuevas cosas en este archivo')#leyo y escribio en el archivo .txt
    file_3.write('nuevas cosas en este archivo\n')#Agregarlo con un salto de linea
    file_3.write('otra linea\n')
    #Nota: por mas que queramos agregar mas lineas al .txt, no va a dejar, ya que siempre va a estar 
    #reemplazando los datos del archivo por unos nuevos que nosotros hayamos escrito

#Leer un archivo csv

import csv

def read_csv(path):
    with open(path,'r') as csvfile:#Abrir la ruta del archivo en formato de lectura
        reader = csv.reader(csvfile, delimiter = (','))#creamos un lector para el archivo, indicando el delimitador
        header = next(reader)#nombre de las columnas se encuentra en la primera fila
        data = []
        for row in reader:
            iterable = zip(header,row)# une los valores de la listas en tuplas
            country_dict = {key: value for key, value in iterable}#Para convertir las tuplas en forma de de diccionario
            #Aunque tamien es posible usar el metodo dict()
            data.append(country_dict)
        return data


if __name__ == '__main__': 
    data = read_csv('Pyhton Basico/data.csv') #Lee el archivo en forma de filas y en listas
    print(data)