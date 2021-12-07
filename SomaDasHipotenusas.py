import math


def e_hipotenusa(numero):
    x=y=1
    while x<numero:
        y=x
        while y<numero:
            if x*x+y*y==numero*numero:
                return True
            y+=1
        x+=1
    else:
        return False

def soma_hipotenusas(n):
    soma=0
    numero=1
    while numero<=n:
        if e_hipotenusa(numero)==True:
            soma+=numero
        numero+=1
    return soma
