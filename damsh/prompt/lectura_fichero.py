import Damsh as d

def lectura(fichero):
    with open(fichero) as file:
        for line in file:
            d.ejecutar_linea(line)

