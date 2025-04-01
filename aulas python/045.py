# Crie um programa que faça you computador jogar jokenpô com você
import random

lista = ("pedra", "papel", "tesoura")
robo = random.randint(0, 2)
print(""" JOKENPO
          [0] PEDRA
          [1] PAPEL
          [2] TESOURA""")
you = int(input("Qual é a sua jogada? "))
print("JO")
print("KEN")
print("po")
print("-=" * 11)
print(f"Você jogou {lista[you]}")
print(f"adversario jogou {lista[robo]}")
print("-=" * 11)
if robo == 0:
    if you == 0:
        print("EMPATE")
    elif you == 1:
        print("VITÓRIA")
    elif 0 == 1:
        print("DERROTA ")
elif robo == 1:
    if you == 0:
        print("DERROTA")
    elif you == 1:
        print("EMPATE")
    elif you == 2:
        print("VITÓRIA")
elif robo == 2:
    if you == 0:
        print("VITÓRIA")
    elif you == 1:
        print("DERROTA")
    elif you == 2:
        print("EMPATE")
