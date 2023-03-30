import csv
def read_csv(path):
    with open(path,'r') as csvfile:#Abrir la ruta del archivo en formato de lectura
        reader = csv.reader(csvfile, delimiter = (','))#creamos un lector para el archivo, indicando el delimitador
        header = next(reader)#nombre de las columnas se encuentra en la primera fila
        data = []
        for row in reader:
            iterable = zip(header,row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


if __name__ == '__main__': 
    data = read_csv('Pyhton Basico/data.csv') #Lee el archivo en forma de filas y en listas
    print(data)