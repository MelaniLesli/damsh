import subprocess, shlex

def ejecutar_linea(linea):
    x = shlex.shlex(linea, punctuation_chars=True)
    x.whitespace_split = True
    arg_list = list(x)
    if len(arg_list) == 0:
        return


    pro = subprocess.run(arg_list)
    

def ejecuto_linea_fich(linea):
    x = shlex.shlex(linea, punctuation_chars=True)
    x.whitespace_split = True
    arg_list = list(x)
    pro = subprocess.run(arg_list) 
