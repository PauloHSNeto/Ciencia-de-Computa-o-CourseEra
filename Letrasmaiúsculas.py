def maiusculas(frase):
    maiusculas=""
    for x in frase:
        if 65<ord(x)<97:
            maiusculas+=x
    return maiusculas



print(maiusculas('PrOgRaMaMoS em python!'))