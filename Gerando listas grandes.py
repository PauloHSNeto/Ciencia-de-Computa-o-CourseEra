import random as rand
def lista_grande(n):
    lista = rand.sample(range(n),n)
    return lista

n=int(input("Digite o valor n:"))
print(lista_grande(n))