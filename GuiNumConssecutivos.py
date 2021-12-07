n = int(input("Digite um número inteiro: "))

a = b = 0
repete = False
while n > 0:
    b = a
    a = n % 10
    n = n // 10
    if b == a:
        repete = True
if repete:
    print("sim")
else:
    print("não")
