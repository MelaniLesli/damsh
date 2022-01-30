
import subprocess, shlex
import sys

import Damsh
import iteractivo as i
import lectura_fichero as lc
import help as h
def inicio():
    if len(sys.argv) == 1:
        i.ejecutando_modo_iteractivo()
    elif len(sys.argv) == 2:
        lc.lectura()
    elif len(sys.argv) >=3 and sys.argv[0] == ' -h':
        h.show_help()
        print('hola')
"""Ejecutar el main"""
if __name__ == "__main__":
    
    inicio()
