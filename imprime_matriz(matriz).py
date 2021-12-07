def imprime_matriz(minha_matriz):
    linhas=len(minha_matriz)
    colunas=len(minha_matriz[0])
    for i in range(linhas):
        print()
        for j in range(colunas):
            print(minha_matriz[i][j], end=" ")
