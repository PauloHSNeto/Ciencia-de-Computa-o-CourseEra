def computador_escolhe_jogada(n,m):
    if n%(m+1)==0:
        return n-(m+1)
    else:
        return m
def usuario_escolhe_jogada(n,m):
    escolha = int(input("Quantas peças você vai tirar?"))
    while(escolha>m):
            escolha=int(input("Oops! Jogada inválida! Tente de novo."))
    return escolha
def partida():
    vez = ""
    Njogador= 0
    Ncomputador=0
    n=nincial=int(input("Quantas peças?"))
    m=mincial=int(input("Limite de peças por jogada?"))
    if n%(m+1)==0:
       print("Você começa!")
       vez ="Jogador"
    else:
       print("Computador começa!")
       vez ="Computador"
    while n>0:
        if vez=="Jogador":
            escolhajogador=usuario_escolhe_jogada(n,m)
            Njogador=Njogador+escolhajogador
            n=n-escolhajogador
            if escolhajogador==1:
                print("Você tirou uma peça")
            else:
                print("Voce tirou {} peças.".format(escolhajogador))
            vez="Computador"
        else:
            escolhacomputador=computador_escolhe_jogada(n,m)
            Ncomputador=Ncomputador+int(computador_escolhe_jogada(n,m))
            n=n-usuario_escolhe_jogada(n,m)
            n=n-escolhacomputador
            if escolhacomputador==1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou {} peças.".format(escolhacomputador))
            vez="Jogador"
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam {} peças no tabuleiro.".format(n))
    if (Njogador>Ncomputador):
            print("Fim do jogo!O jogador ganhou!")
    else:
        print("Fim do jogo! O computador ganhou!")

modoDeJogo= int(input("Bem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato"))
if modoDeJogo==1:
    print("Voce escolheu uma partida única!")
    partida()
else:
    print("Voce escolheu um campeonato!!")
    placarJogador=0
    placarComputador=0
    campeonatos=3
    while campeonatos>0:
        partida()
        if partida()==print("Fim do jogo!O jogador ganhou!"):
            placarJogador=placarJogador+1
        else:
            placarComputador=placarComputador+1
        campeonatos=campeonatos-1
    print("**** Final do campeoato! ****\n Placar: Você {} X {} Computador".format(placarJogador,placarComputador))


