import argparse

parser = argparse.ArgumentParser()
parser.add_argument("n", type= int)
args= parser.parse_args()
n= args.n 

if n<=0:
    print("El número no es válido. Ingrese un número natural.")
elif n<=2:
    print(f"El número {n} es primo.")
else:
    compuesto = False
    divisor = 2
    
    while divisor<n:
        if n%divisor == 0:
            compuesto = True
            break
        divisor += 1
    if not compuesto:
        print(f"El número {n} es primo.")
    else:
        print(f"El numero {n} es compuesto.\nSe cumple que {divisor}*{int(n/divisor)} = {n}")