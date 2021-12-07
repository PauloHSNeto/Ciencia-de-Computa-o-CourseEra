largura=l=int(input("digite a largura: "))
altura=a=int(input("digite a altura: "))
while altura>0:
    largura=l
    while largura >0:
        if (altura==a or altura ==1):
           print("#", end="")
        else:
            if largura==1 or largura ==l:
                print("#", end="")
            else:
                print("", end=" ")
        largura-=1
    print()
    altura-=1
                        