# Crie um programa que vai ler vários números e coloque-os em uma lista 
# Depois disso, crie duas listas extras que vão contar apenas os valores pares e os impares digitados, respectivamente:
# Ao final, mostre o conteúdo das três listas geradas ]
lista = []
impar = []
par = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    op = input('Você quer continuar?S/N ').upper()
    if op == 'S':
        continue
    else:
        break
lista.sort()
impar.sort()
par.sort()
print(f'A lista principal é {lista}')
print(f'A lista contendo apenas números pares é {par}')
print(f'A lista contendo apenas números impares é {impar}')