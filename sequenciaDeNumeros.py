sequencia=[]
numero=1
while numero!=0:
    numero = int(input("Digite um número:"))
    sequencia.append(numero)
indice=len(sequencia)-2

while indice>=0:
    print(sequencia[indice])
    indice-=1
