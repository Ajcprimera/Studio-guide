import utils_2
import Poplation
import Dia_15
def run():
    data = Poplation.read_csv('Pyhton Basico/data.csv')
    country = input('Ingrese un pais: ')
    #countries = list(map(lambda x: x['Country/Territory'], data))
    #percentages = list(map(lambda x: x['World Population Percentage'], data))
    
    #Dia_15.generate_pie_chart(countries, percentages)
    result = utils_2.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils_2.get_population(country)
        Dia_15.generate_bar_chart(labels, values)

if __name__ == '__main__': 
    run()