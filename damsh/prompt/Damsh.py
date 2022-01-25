import subprocess, shlex

class Damsh():
    def ejecutar_linea(self, linea):
        x = shlex.shlex(linea, punctuation_chars=True)
        x.whitespace_split = True
        arg_list = list(x)

        pro = subprocess.run(arg_list)

