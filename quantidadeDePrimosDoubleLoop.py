def n_primos (x):
    numero =2
    quantidadeDePrimos=0
    while numero<=x:
        divisor = 2
        divisores=0
        while divisor<numero:
            if numero%divisor==0:
               divisores+=1
            divisor+=1
        if divisores==0:
            quantidadeDePrimos+=1
        numero+=1
    return quantidadeDePrimos