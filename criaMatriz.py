def cria_matriz(linhas, colunas, valor):
    matriz=[]
    for i in range(linhas):
        linhas=[]
        for j in range(colunas):
            linhas.append(valor)
            valor+=1
        matriz.append(linhas)



    return matriz
i=0
while i<len(cria_matriz(8, 8, 0)):
    print("{}\n".format(cria_matriz(8, 8, 0)[i]))
    i+=1        
