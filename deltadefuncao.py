import math

a = int(input("digite o valor do coeficiente de x^2:"))
b = int(input("digite o valor do coeficiente de x:"))             
c = int(input("digite o valor do coeficiente de final:"))             
delta = b*b-4*a*c
if math.sqrt(delta)>0:print("a função possui duas raizes reais")
if math.sqrt(delta)==0:print("a função possui uma raiz")
if math.sqrt(delta)<0:print("a função não possui raizes reais")
