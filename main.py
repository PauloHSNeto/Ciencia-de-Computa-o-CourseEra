def computador_escolhe_jogada (n,m):
    if n%(m+1)==0:
        return n-(m+1)
    else:
        return m

def usuario_escolhe_jogada (n,m):
    user = int(input:("Digite a sua jogada:"))
    while 1>user>m:
        print("Erro. Digite uma jogada válida:")
    return user




def partida ():
    n=int(input("Digite N:"))
    m=int(input("Digite M"))
    if n%(m+1)!=0:
        return print("Você começa!")
    else:
