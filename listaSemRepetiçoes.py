def remove_repetidos(lista):
    novalista=[]
    for x in lista:
        if x not in novalista:
            novalista.append( x)
    return sorted(novalista)
