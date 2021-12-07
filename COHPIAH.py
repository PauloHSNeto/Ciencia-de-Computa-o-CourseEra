import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    resultado=0
    indice=0
    while indice<6:
        resultado+=(abs(as_a[indice]-as_b[indice])/6)
        indice+=1
    return resultado
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas=separa_sentencas(texto)
    frases=[]
    lista_palavras=[]
    for sentenca in sentencas:
        frases.append(separa_frases(str(sentenca)))
    for frase in frases:
        lista_palavras.append(separa_palavras(str(frase)))
    tamanhos_das_palavras=0
    for palavra in lista_palavras:
        tamanhos_das_palavras+=len(palavra)
    somaDosCaracteresDasSentencas=0
    for sentenca in sentencas:
        somaDosCaracteresDasSentencas+= len(sentenca)
    somaDosCaracteresDasFrases=0
    for frase in frases:
        somaDosCaracteresDasFrases+=len(frase)


    ass_a=[1,2,3,4,5,6]
    ass_a[0]=float(tamanhos_das_palavras/len(lista_palavras))
    ass_a[1]=float(n_palavras_diferentes(str(lista_palavras))/len(lista_palavras))
    ass_a[2]=float(n_palavras_unicas(str(lista_palavras))/len(lista_palavras))
    ass_a[3]=float(somaDosCaracteresDasSentencas/len(sentencas))
    ass_a[4]=float(len(frases)/len(sentencas))
    ass_a[5]=float(somaDosCaracteresDasFrases/len(frases))
    return ass_a

    pass

def avalia_textos(textos, ass_cp):

    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    graus=[]
    for texto in textos:
        graus.append(compara_assinatura(calcula_assinatura(texto), ass_cp))
    return graus.index(min(graus))+1
    pass
