import shlex, subprocess, sys
import Damsh as d

def lectura():
    with open(sys.argv[1]) as file:
        for line in file:
            d.ejecutar_linea_fich(line)

