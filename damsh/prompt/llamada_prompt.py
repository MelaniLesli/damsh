import subprocess, shlex, sys

import Damsh
import iteractivo as i
import lectura_fichero

"""Ejecutar el main"""
if __name__ == "__main__":
    if(len(sys.argv) == 1):
        i.ejecutando_modo_iteractivo()
