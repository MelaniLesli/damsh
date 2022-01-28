import subprocess, shlex
import Damsh as x
"""
class Damsh():
    def ejecutar_linea(self, linea):
        # 1. Parsear linea shlex
        s = shlex.shlex(linea, punctuation_chars=True)
        s.whitespace_split = True
        arg_list = list(s)
        ret = subprocess.run(arg_list)
"""
def ejecutando_modo_iteractivo():
     while True:
        linea = input('damsh> ')
        x.ejecutar_linea(linea)
    
