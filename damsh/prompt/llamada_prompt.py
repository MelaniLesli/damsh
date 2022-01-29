çimport subprocess, shlex, sys

import Damsh
import iteractivo as i
import lectura_fichero as lc
def inicio():
    if len(sys.argv) == 1:
        i.ejecutando_modo_iteractivo()
    elif len(sys.argv) == 2:
        lc.lectura()
        return
"""Ejecutar el main"""
if __name__ == "__main__":
    inicio()
#    if len(sys.argv) == 1:
#        i.ejecutando_modo_iteractivo()
#       return
#    elif len(sys.argv) ==1:
#      i.ejecutando_modo_iteractivo()
