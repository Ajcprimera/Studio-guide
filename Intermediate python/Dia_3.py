#encapsulacion

'''
Nos ayuda a agrupar datos y su comportamiento 
en un mismo lugar, ademas de controlar el acceso
de esos datos, evitando que se modifiquen directamente
En Python no existe, pero se puede simular precediendo atributos 
y métodos con  dos barras bajas __ como indicando 
que son "especiales".
'''

class CasilladeVotacion:
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property #decoradores
    def region(self):
        return self._region
    
    @region.setter
    def region (self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self._pais}')

casilla = CasilladeVotacion(123, ['Mexico', 'Ciudad de Mexico'])#identificador, region del pais
print(casilla.region)

casilla.region = 'Ciudad de Mexico'
print(casilla.region)
'''
Nota: No es recomendable usar Encapsulamiento en POO de python
ya que solemos perder lo esencial de python, flexibilidad y 
generacion de polimorfismos y la manera de acceder a estos
datos es creando metodos publicos con getter y setter
'''

#herencia
'''
La herencia sucede cuando tenemos una clase superior y de  esa clase 
superior queremos pasarle los metodos y atributos a una clase derivada,
este metod tambien nos ayuda en la reutilizacion de codigo en diversas
maneras
'''

'''
Muestra de herencia de clases:
class Clase_Principal:
    metodos y atributos de Clase_Principal

class Clase_Derivada(Clase_Principal):
    metodos y atributos de Clase_Derivada

Como podemos ver Clase_Derivada hereda los metodos de la
Clase_Principal
'''

#ejemplo
class Cuadrilatero:
    def __init__(self, lados):
        self.lados = lados
        self.suma_angulos = 360

    def perimetro(self):
        return sum(self.lados)
    
class Cuadrado(Cuadrilatero):
    def __init__(self, lados):
        super().__init__(lados)

cuadrado1 = Cuadrado([4,4,4,4])

perimetro = cuadrado1.perimetro()
print(perimetro)

#Herencia multiple
'''
Uba clase, puede derivarse de mas de una clase y la caracteristicas de 
toda esa clase se heredan
'''

#Ejemplo

class Base1:
    pass

class Base2:
    pass

class Multi(Base1, Base2):
    pass

'''
Nota: tambien podemos heredar de una clase derivada
'''

#ejemplo

class Base:
    pass

class Derivada(Base):
    pass

class Derivada2 (Derivada):
    pass