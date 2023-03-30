#Libreria que creamos con diversas funciones que podemos usar
def get_population():
    keys = ['col','bol']
    values = [200, 300]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result