import subprocess, shlex, sys

import Damsh
import iteractivo as i
import lectura_fichero
def vacio():
    while True:
        linea = input('damsh')


"""Ejecutar el main"""
if __name__ == "__main__":
    if len(sys.argv) == 0:
        vacio()
    elif len(sys.argv) ==1:
        i.ejecutando_modo_iteractivo()
