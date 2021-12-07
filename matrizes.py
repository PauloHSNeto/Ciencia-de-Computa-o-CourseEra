def dimensoes(matriz):
    linhas =len(matriz[:])
    colunas =len(matriz[0])
    dim=str(linhas)+"X"+str(colunas)
    print (dim)

matriz=input("digite a matriz:")
dimensoes(matriz)