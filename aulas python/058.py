# melhore o jogo do desafio 028 onde o computador vai pensar em um numero entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acerta.mostrando no final quantos palpites
# foram necessários para vencer
#
from random import randint

n = randint(0, 10)
palpite = 1
while True:
    s = int(input("Tente adivinhar o número do computador(0 a 10):  "))
    if s != n:
        print("você errou, tente outro palpite")
        palpite += 1
    else:
        print(f"Você acertou o número com {palpite} tentativas")
        break
