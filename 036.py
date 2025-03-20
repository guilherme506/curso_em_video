# Escreva um programa para aprovar o empréstimo bancário para a compre de uma casa.
# O programa vai perguntar o valor da casa
# o salario do comprador e em quantos anos ele vai pagar
#
# calcule o valor da prestação mensal. sabendo que ela não pode exceder 30%
# do salario ou então o empréstimo será negado
from math import floor
casa = int(input('Qual é o valor da casa: '))
salario = int(input('Qual é o seu salário: '))
tempo = int(input('Em quantos anos você quer pagar: '))
n = salario * (30/100)
p = floor((casa / tempo)/12)
if p < n:
    print(f'Seu empréstimo foi aprovado!, o valor da prestação mensal é de {p} reais')
else:
    print('Seu empréstimo foi recusado')