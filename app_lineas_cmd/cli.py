#Script para renombrar un archivo
import sys

def cli(args):
    if len(args) == 1:
        print("No se han pasado argumentos")
        return
    if len(args) != 3 :
        print("Se necesitan dos argumentos")

cli(sys.argv)