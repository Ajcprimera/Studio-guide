#   Graficas en python
import matplotlib.pyplot as plt

def generate_bar_chart(labels, values): #Graficas en forma de barras
    
    fig, ax = plt.subplots()#fig = la figura; ax = las coordenadas que vamos a graficar
    #El comando plt.subplots() crea 2 objetos: una Figure fig (figura) que es un contenedor de todo lo que verás en el gráfico 
    # y los Axes ax (ejes) que contienen la información a graficar
    ax.bar(labels, values)#Para mostrar en formas de barras
    plt.show()#mostrar grafica

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)#la manera en que debemos indicar el argumento labels en la libreria
    ax.axis('equal')#para mostrarla de formar centrada y en forma de circulo
    plt.show()

if __name__ == '__main__':#Mostrarlo en forma de script
    labels = ['a', 'b','c']
    values = [100,200,80]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)