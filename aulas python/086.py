# Crie um programa que crie uma matriz 3 x 3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tela, com a formatação correta.
lista = list()
lista2 = list()
lista3 = list()
tot = list()
for c in range(0, 3):
    n = int(input(f"Digite um número para [0,{c}]: "))
    lista.append(n)
for v in range(0, 3):
    num = int(input(f"Digite um número para [1,{v}]: "))
    lista2.append(num)
for b in range(0, 3):
    num2 = int(input(f"Digite um número para [2,{b}]: "))
    lista3.append(num2)
tot.append(lista[:])
tot.append(lista2[:])
tot.append(lista3[:])
print(f"{tot[0]}")
print(f"{tot[1]}")
print(f"{tot[2]}")
