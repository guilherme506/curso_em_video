# Faça um programa que ajude um jogador da mega sena, A criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
lista = list()
jogos = list()
cont = 0
n = int(input('Quantos jogos vocẽ vai querer jogar: '))
for c in range(0,n):
    while True:
        num = randint(0,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
lista.sort()   
jogos.append(lista[:])
lista.clear()

print(lista)