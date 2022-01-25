import shlex, subprocess, sys
from Damsh as lector_fich

def lectura():
    
    with open(sys.argv[1]) as file:
    #Añadir condicional con retorno de carro '/ o *'
        for line in file:
            lector_fich.ejecutar_linea(line)

