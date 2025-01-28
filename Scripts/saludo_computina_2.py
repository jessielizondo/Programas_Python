import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-mensaje","--m", default="")
args = parser.parse_args()

texto = str(args.m)

value = random.random()

if texto == "Hola" or texto == "HOLA":
    if value <= 0.5:
        print("Hola, cómo estas?")
    elif value <= 0.75:
        print('Hola, me llamo Computina')
    else:
        print("Háblale a la mano")

else:
    print("Primero, saluda!!")