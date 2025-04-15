# Faça um programa que leia nome e peso de varías pessoas, guardando tudo em uma lista.No final mostre :
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves
pessoa = list()
lista = list()
maior = menor = 0
while True:
    pessoa.append(str(input("Digite um nome: ")))
    pessoa.append(float(input("Dgite o peso: ")))
    if len(lista) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    c = str(input("Quer continuar(S/N): ")).upper()
    if c == "S":
        continue
    else:
        break
print('-=' * 30)
print(f"A quantidade de pessoas cadastradas foram de {len(lista)}")
print(f"O maior peso registrado foi {maior}kG. Peso de ", end="")
for p in lista:
    if p[1] == maior:
        print(f"[{p[0]}]", end="")
print()
print(f"O menor peso registrado foi {menor}KG. Peso de ", end="")
for p in lista:
    if p[1] == menor:
        print(f"[{p[0]}]", end="")
print()
# oberservação, pode usar contador ou len pra saber quantos cadastros
