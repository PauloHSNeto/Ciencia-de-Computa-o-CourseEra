def fatorial(x):
    valor=1
    
    while x>0:
        valor = valor*x
        x= x-1
    return valor
def binomial (x,y):
    valor = fatorial(x)/(fatorial(y)*fatorial(x-y))
    return valor
