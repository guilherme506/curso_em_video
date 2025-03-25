# Faça um programa que leia o peso de cinco pessoas
# no final, mostre qaul foi o maior e o menos peso lidos
#
lista_peso = []
for pessoa in range(1, 6):
    n = float(input(f"O peso da {pessoa}° pessoa: "))
    lista_peso.append(n)
peso_maior = max(lista_peso)
peso_menor = min(lista_peso)
print(f"O maior peso comentado foi de {peso_maior}Kg")
print(f"O meno peso comentado foi de {peso_menor}Kg")
