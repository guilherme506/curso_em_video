# Crie um programa que leia o ano de nascimento de sete pessoas
# no final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores
# maioridade 21 anos
#
from datetime import date

atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nascimento = int(input(("Em que ano você nasceu: ")))
    idade = atual - nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f"A quantidade de pesosas que são maiores de idade é de {maior}")
print(f"A quantidade de pessoas que são menores de idade é de {menor}")
