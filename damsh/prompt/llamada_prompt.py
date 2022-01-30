"""Inicio"""
import subprocess, shlex
import sys

from interactivo import ejecutando_modo_interactivo
from lectura_fichero import lectura
from help import show_help


def inicio():
    if len(sys.argv) == 1:
        ejecutando_modo_interactivo()
    elif len(sys.argv) == 2:
        lectura(sys.argv[1])
    elif len(sys.argv) >= 2 and sys.argv[1] == '-h':
        show_help()
   
