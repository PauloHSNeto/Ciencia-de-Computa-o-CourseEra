def soma_elementos(x):
    soma=0
    for n in x:
        soma+=int(n)
    return soma
x=input("Digite x")
print(soma_elementos(x))
