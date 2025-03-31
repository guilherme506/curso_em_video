# Crie um programa que leia a idade e o sexo de várias pessoas
# A cada pessoa cadastrada. O programa deverá perguntar se o usuário quer ou não continuar.
# No final,mostre:
# A) quantas pessoas tem mais de 18 anos
# B) quantos homens foram cadastrado
# C)Quantas mulheres foram cadastrada com menos de 20 anos
p18 = h = f = 0
while True:
    print('Cadastro de pessoa')
    idade = int(input('Idade da pessoa: '))
    sexo = str(input('Qual é o gênero da pessoa(M/F): ')).upper().strip()[0]
    if idade >= 18:
        p18 += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        f += 1
    print('=-=' * 20)
    print('Você quer cadastrar mais pessoas?')
    resposta =str(input('resposta(S/N): ')).upper().strip()[0]
    print('=-=' * 20)
    if resposta == 'N':
        break
print(f'A quantidade de pessoas com mais de 18 anos e de {p18}')
print('=_=' * 20)
print(f'A quantidade de homens que foram cadastrados e de {h}')
print('=_=' * 20)
print(f'A Quantidade de mulheres com menos de 20 anos cadastradas e de {f}')
print('=_=' * 20)