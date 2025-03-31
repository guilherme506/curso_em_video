# Escreva um programa que faça o computador 'pensar' em um nuemro inteiro
# entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador
#
# o programa deverá escrever na tela se o usuário venceu ou perdeu
#
from random import randint

s = int(input("Qual número entre 0 a 5 que o compuatador escolheu: "))
n = randint(0, 5)
if n == s:
    print("Parabens você acertou")
else:
    print(f"Você errou que pena o computador escolher {n}")
