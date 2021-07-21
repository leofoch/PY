import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError ("El nro no puede ser negativo")
    else:
        return math.sqrt(num1)

opt1= (int(input("Ingrese nro: ")))

try:
    print(calculaRaiz(opt1))
except ValueError as ErrorNroNegativo:
    print(ErrorNroNegativo)
    
print("sigue el programa")
