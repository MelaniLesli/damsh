import subprocess, shlex, sys

import Damsh
import iteractivo as i
import lectura_fichero as lc
def vacio():
    if len(sys.argv) == 1:
        i.ejecutando_modo_iteractivo()
        return
    elif len(sys.argv) == 2:
        lc.lectura()
        return
"""Ejecutar el main"""
if __name__ == "__main__":
    vacio()
#    if len(sys.argv) == 1:
#        i.ejecutando_modo_iteractivo()
#       return
#    elif len(sys.argv) ==1:
#      i.ejecutando_modo_iteractivo()
