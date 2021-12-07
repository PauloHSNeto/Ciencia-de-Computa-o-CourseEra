n=int(input("Digite um número inteiro: "))
divisor=2
while divisor<n:
    if n%divisor==0:
        print("não primo")
        break
    else:
        divisor=divisor+1
else: print("primo")


    
    
