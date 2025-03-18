# Faça um programa que leia um número de 0 a 9999
# E mostre na tela cada um dos digitos separados
# Ex:digite um número: 1834
# Unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
#string e math

# METODO DE STRING:
#n = int(input('digite um numero de 0 a 9999: '))
#s = str(n)
#print(f'Analisando o numero {n} temos:')
#print(f'Unidade: {s[3]}')
#print(f'Dezena: {s[2]}')
#print(f'Centena: {s[1]}')
#print(f'Milhar: {s[0]}')

# METODO DE MATEMATICA:
n = int(input('digite um numero de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Ao analisar o numero {n} temos : ')
print(f'unidade:{u} ')
print(f'dezena:{d} ')
print(f'centena:{c} ')
print(f'milhar:{m} ')