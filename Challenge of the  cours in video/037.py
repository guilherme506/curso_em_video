# Escreva um programa que leia um número inteiro qualquer
# e peça para o usúario escolher qual será a base de conversão
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal 
n = int(input('Digite um número inteiro: '))
option= int(input('''escolha uma:
                  [1]-binario
                  [2]-octal
                  [3]-hexadecimal 
                  opção: '''))
binario = bin(n)
octal = oct(n)
hexadecimal = hex(n)
if option == 1:
    print(f'O seu número em Binário é {binario}')
elif option == 2:
    print(f'O seu número em octal é {octal}')
elif option == 3:
    print(f'O seu número em Hexadecimal é {hexadecimal}')
else:
    print('Você não escolheu uma opção, retorne e escolha alguma opção')