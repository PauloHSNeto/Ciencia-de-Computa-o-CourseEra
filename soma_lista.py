def soma_lista(lista):
    if len(lista)==0:
        return 0
    elif len(lista)==1:
        return lista[0]
    meio=len(lista)//2
    return soma_lista(lista[:meio])+soma_lista(lista[meio:])




a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17]
print(soma_lista(a))