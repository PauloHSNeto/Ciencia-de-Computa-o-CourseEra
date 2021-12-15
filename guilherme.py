import random
import time
from random import randint
from time import sleep
pc = randint(0, 10)
print("Sou seu computador UHAAA...{} Acabei de pensar em um número entra 0 e 10.")
sleep(6)
print("Será que você, mero mortal consegue adivinhar??? ")
sleep(4)
acertou = False
palpite = 0
while not acertou:

    jogador = float(input("Qual é seu palpite?: "))
    palpite += 1
    if jogador == pc:
        acertou = True
        print("Acertou mizeravi!")
    else:
        if jogador < pc:
            print("Mais... Tente novamente")
        elif jogador > pc:
            print("Menos... tente novamente")
print(f"Você precisou de {palpite} tentativas ")

