# Aprimore o desafio anterior, mostrando no final :
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha
lista = list()
lista1 = list()
lista2 = list()
par = list()
par1 = list()
par2 = list()
tot = list()
for c in range(0, 3):
    n = int(input(f"Digite um número para [0,{c}]: "))
    if n % 2 == 0:
        par.append(n)
        lista.append(n)
    else:
        lista.append(n)
for v in range(0, 3):
    n1 = int(input(f"Digite um número para [1,{v}]: "))
    if n1 % 2 == 0:
        par1.append(n1)
        lista1.append(n1)
    else:
        lista1.append(n1)
for b in range(0, 3):
    n2 = int(input(f"Digite um número para[2, {b}]: "))
    if n2 % 2 == 0:
        par2.append(n2)
        lista2.append(n2)
    else:
        lista2.append(n2)
tot.append(lista), tot.append(lista2), tot.append(lista1)
print(tot[0])
print(tot[2])
print(tot[1])
print(f"A soma de todos os números pares são {sum(par) + sum(par1) + sum(par2)}")
print(f"A soma dos valores da terceira coluna é {tot[0][2] + tot[1][2] + tot[2][2]}")
print(f"O maior valor da segunda linha linha é {max(tot[2])}")
