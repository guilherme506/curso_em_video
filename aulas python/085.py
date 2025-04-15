# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente 
lista = [ [] , []]
valor = 0
for c in range(1, 8):
    valor = (int (input(f'Digite o {c}° número: ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('-=' * 30)
print(f'Os seus números foram {lista}')
print('-=' * 30)
print(f'Os números pares foram {lista[0]}')
print('-=' * 30)
print(f'Os números impares são {lista[1]}')