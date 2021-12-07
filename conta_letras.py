def conta_letras(frase, contar="vogais"):
    frase
    numero=0
    if contar == "consoantes":
        for indice in range(len(frase)):
          if (frase[indice]!= "a" and frase[indice]!= "e" and frase[indice]!= "i" and frase[indice]!= "o" and frase[indice]!= "u") and 123>ord(frase[indice])>64:
            numero+=1
    else:
        for indice in range(len(frase)):
            if (frase[indice]== "a" or frase[indice]== "e" or frase[indice]== "i" or frase[indice]== "o" or frase[indice]== "u") and 123>ord(frase[indice])>64:
                numero += 1

    return numero

print(conta_letras('programamos em python', 'consoantes'))