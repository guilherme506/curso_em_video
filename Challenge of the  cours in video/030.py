# crie um programa que leia um número inteiro e mostre se 
# na tela se eele é PAR ou ÍMPAR
#
#
n = int(input('Digite um número: '))
par = n%2
if par == 0:
    print('seu numero é par')
else:
    print('seu numero e impar')