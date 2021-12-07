def primeiro_lex(lista):
    for palavras in lista:
        palavras=palavras.strip()

    listaOrdenada=sorted(lista)
    return listaOrdenada[0]