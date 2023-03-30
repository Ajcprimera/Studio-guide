import utils #Una libreria que creamos nosotros mismo con varias funciones

data = [
    {'Country': 'Colombia',
    'Population': 300},
    {'Country': 'Bolivia',
    'Population': 400}
    ]

def run():
    country = input('Ingrese un pais: ')
    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__': 
    '''
    Esta condicion es muy importate nos permite hacer la dualidad de los modulos, ya que
    nos ejecutar este modulo sin la necesidad de hacerlo en el example.py
    ''' 
    run()