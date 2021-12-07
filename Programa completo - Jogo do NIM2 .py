def computador_escolhe_jogada(n,m):
        escolha = 1
        while escolha != m:
                if (n-escolha)%(m+1)==0:
                        return escolha
                else:
                        escolha += 1
        return escolha


def usuario_escolhe_jogada(n,m):
    escolha= int(input("Quantas peças você vai tirar?"))
    while escolha > m or escolha <1 or escolha>n:
        print("Oops! Jogada inválida! Tente de novo.")
        escolha = int(input("Quantas peças você vai tirar?"))
    return escolha

def partida():
    vez = ""
    Njogador= 0
    Ncomputador=0
    n=int(input("Quantas peças?"))
    m=int(input("Limite de peças por jogada?"))
    if (n)%(m+1)==0:
        print("Você começa!")
        vez ="Jogador"
    if (n)%(m+1)!=0:
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
        if vez=="Computador":
                escolhacomputador=computador_escolhe_jogada(n,m)
                Ncomputador=Ncomputador+escolhacomputador
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
    if vez!="Jogador":
        print("\nFim do jogo!O jogador ganhou!")
    else:
        print("\nFim do jogo! O computador ganhou!")

modoDeJogo= int(input("Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato"))
if modoDeJogo==1:
    print("Voce escolheu uma partida única!\n")
    partida()
else:
    print("Voce escolheu um campeonato!!\n")
    placarJogador=0
    placarComputador=0
    campeonatos=1
    while campeonatos<4:
                print('\n**** Rodada {} ****\n'.format(campeonatos))
                partida()
                campeonatos=campeonatos+1
    print("**** Final do campeoato! ****\n Placar: Você {} X 3 Computador".format(placarJogador,placarComputador))
