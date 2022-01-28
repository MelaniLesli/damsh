import subprocess, shlex

def ejecutar_linea(linea):
    x = shlex.shlex(linea, punctuation_chars=True)
    x.whitespace_split = True
    arg_list = list(x)
    pro = subprocess.run(arg_list, capture_output=True)
    
