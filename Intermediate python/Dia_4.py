#Polimorfismos

'''
Esta nos permite cambiar el comportamiento de 
una superclase para adaptarlo a la subclase

La manera en que se puede hacer es demasiado sencilla y
es tomando el nomber del metodo de la superclase que 
queremos implementar a la subclase
'''

#ejemplo

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar (self):
        print('Ando caminando')

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanzar (self):
        print('Ando con mi bicicleta')

def main():    
    persona1 = Persona('Lucas')
    persona1.avanzar()

    persona2 = Ciclista('Luis')
    persona2.avanzar()

main()

#Complejidad algoritmica
'''
es aquella que nos permite determinar la complejidad del
algoritmo, mayormente, esta complejidad es medida mediante
unidades de tiempo, permitiendo comparar la eficiencia entre
algoritmos
'''

#ejemplo con sucesion de fibonacci
import time

def factorial(n):
    respond = 1
    while n >1:
        respond *= n
        n-= 1
    return respond

def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n-1)

if __name__ == '__main__':
    n = 2

    
    start = time.time()
    factorial(n)
    end = time.time()
    print(end - start)

    start = time.time()
    factorial_r(n)
    end = time.time()
    print(end - start)

#Notacion asintotica

'''
Nos permite analizar el tiempo djecucion de un algoritmo
identificando su comportamiento si el tamaño de entrada 
para el algoritmo aumenta
'''
def f(n):
    for i in range (n):
        for j in range(n):#crecimiento cuadratico
            print(i, j)

f(100)

#Clases de complejidad algoritmica


'''
* O(1)Constante: no importa la cantidad de input que 
reciba, siempre demorara el mismo tiempo.

* O(n)Lineal: la complejidad crecerá de forma proporcional 
a medida que crezca el input.

* O(log n)Logaritmica: nuestra función crecerá de forma 
logarítmica con respecto al input. Esto significa que en 
un inicio crecerá rápido, pero luego se estabilizara.

* O(n log n)log lineal: crecerá de forma logarítmica pero 
junto con una constante.

* O(n**2)Polinomial: crecen de forma cuadrática. No son 
recomendables a menos que el input de datos en pequeño.

* O(2**n)Exponencial: crecerá de forma exponencial, por lo 
que la carga es muy alta. Para nada recomendable en ningún 
caso, solo para análisis conceptual.

* O(n!): crece de forma factorial, por lo que al igual que el 
exponencial su carga es muy alta, por lo que jamas utilizar 
algoritmos de este tipo.
'''