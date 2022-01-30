import subprocess, shlex
import Damsh as x

def ejecutando_modo_interactivo():
     while True:
        linea = input('damsh> ')
        x.ejecutar_linea(linea)
    
