"""Módulo que contiene la guia de nuestro programa """
intro = 'damsh - The Dam shell'
a = 'damsh'
b = 'damsh -h'
c = 'damsh -c COMMAND'
d = 'damsh FILE.dsh'

v = 'Enter the interactive shell'
x = 'Print this help an exit'
y = 'Execute given command and exit '
z = 'Execute commands in the scrip file and exit'

menu1 = [a, b, c, d]
menu2 = [v, x, y, z]

def show_help():
    c = 0
    print(intro)
    for i in menu1:
        print(f" - {i}       {menu2[c]}")
        c = c + 1
