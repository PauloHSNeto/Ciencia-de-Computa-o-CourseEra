def soma_matrizes(m1,m2):
    def dimensoes(matriz):
        linhas =len(matriz[:])
        colunas =len(matriz[0])
        dim=str(linhas)+"X"+str(colunas)
        return dim
    if dimensoes(m1)!=dimensoes(m2):
        return (False)

    matriz_soma=[]
    for i in range(len(m1)):
       linha=[]
       for j in range(len(m1[0])):
            linha.append(m1[i][j]+m2[i][j])
       matriz_soma.append(linha)
    return matriz_soma
