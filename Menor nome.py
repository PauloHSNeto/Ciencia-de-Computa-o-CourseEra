def  menor_nome(nomes):
    menor=""
    for i in range(len(nomes)):
        nomes[i] = nomes[i].strip()
        nomes[i]=nomes[i].capitalize()
    menor=nomes[0]
    print(nomes)
    for i in range(len(nomes)):
        if len(nomes[i])<len(nomes[i-1]):
           menor=nomes[i]
    return menor

print(menor_nome(['zé', ' lu', 'fê']))