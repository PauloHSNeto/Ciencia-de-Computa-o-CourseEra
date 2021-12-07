n=int(input("Digite um número inteiro"))
resto = 0
repete = False
while n>0:
    
    resto=n%100
    n=n//10
    if resto%11==0:
        repete=True


if repete:
    print("sim")
else:
    print("não")    
