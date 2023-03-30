import csv
def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = (','))
        total = 0
        for i in reader:
            total =  total + int(i[1])# Recuerda indicar la fila que quieres sumar
        return total
    

response = read_csv('Pyhton Basico/data_2.csv')
print(response)