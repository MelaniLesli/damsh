import subprocess, shlex
from Damsh as iteractivo


def ejecutando_modo_iteractivo():
    
    while True:
        linea = input('damsh> ')
        iteractivo.ejecutar_linea(linea)
