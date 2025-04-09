# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
#Caso o número já exista lá dentro, ele não sera adicionad.
#No final serão exibidos todos os valores únicos digitados, em ordem crescente
lista = []
while True:
    num = (int(input('Digite um número: ')))
    if num not in lista:
        lista.append(num)
        print('Seu número foi adicionado')
    else:
        print('Valor duplicado, não adicionado')
    op = input('Você quer continuar(S/N): ').upper()
    if op == 'S':
        continue
    else:
        break
lista.sort()
print(f'A sua lista é {lista}')