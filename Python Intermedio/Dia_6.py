#graficado simple mediante bokhe

from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_val = int(input('Cuantos valores desea? '))

    x_vals = list(range(total_val))
    y_vals = []

    for i in x_vals:
        val = int(input(f'Valor para la entrada {i}: '))
        y_vals.append(val)

    fig.line(x_vals,y_vals,line_width = 2)

    show(fig)

'''
El graficado puede ser el mismo que realizamos con la libreria de
matplotlib, sin embargo, bokhe nos ofrece una mayor variedad para
poder graficar lo que deseemos
'''