# Faça um programa que leia um número inteiro
# e diga se ele é ou não um numero primo
#
n = int(input("digite um numero: "))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print("\033[33m", end= ' ' )
        tot += 1
    else:
        print("\033[31m", end= ' ' )
    print(f"{c}", end= ' ' )
print(f"\n\033[O numero {n} foi divísivel {tot} vezes")
if tot == 2:
    print("ele e primo")
else:
    print("ele não e primo")
