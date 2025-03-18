#Faça um algoritmo que leia o preço de um produto e mostra seu novo preco 
#com 5% de desconto
import math
n = float(input('preço do produto: '))
s = n * ( 5 / 100)
v = n - s
print(f'O preço do produto com desconto ficou em {v} reais ')