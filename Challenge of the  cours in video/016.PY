#Crie um programa que leia um número real qualquer pelo teclado 
# e mostre na tela a sua porçaõ inteira
#ex:digite um numero:6.127
#o numero 6.127 tem a parte interia 6
#obs: olhas as funçoes do math

from math import(trunc)
n = float( input('Escreva um numero: '))
print(f'O numero real e {trunc(n)}')