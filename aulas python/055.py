# Faça um programa que leia o peso de cinco pessoas
# no final, mostre qaul foi o maior e o menos peso lidos
#
lista_peso = []
for pessoa in range(1, 6):
    n = float(input(f"O peso da {pessoa}° pessoa: "))
    lista_peso.append(n)
print(f"O maior peso comentado foi de {max(lista_peso)}Kg")
print(f"O meno peso comentado foi de {min(lista_peso)}Kg")
