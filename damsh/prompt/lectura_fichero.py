import shlex, subprocess, sys
import Damsh as lector_fich

def lectura():
    
    with open(sys.argv[1]) as file:
        for line in file:
            lector_fich.ejecutar_linea(line)

