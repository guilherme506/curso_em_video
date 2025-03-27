#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n 
#primeiro elementos de uma sêquencia 
#ex = 0-1-1-2-3-5-8
print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer mostrar: '))
cont = 0
form = 0
while n <= 0:
    print(f'{form}-->',end='')
    form += n
    cont += 1