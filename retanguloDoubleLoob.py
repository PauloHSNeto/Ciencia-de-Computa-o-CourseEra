largura=l=int(input("digite a largura: "))
altura=a=int(input("digite a altura: "))
while altura>0:
    largura=l
    while largura>0:
        print("#", end="")
        largura-=1
    print()
    altura-=1