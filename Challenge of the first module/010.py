#Crie um programa que leia quanto dinheiro uma pessoa  tem na carteira
#E mostre quantos dolares ela pode comprar 
import math
n = float(input('quantos de dinheiro vocẽ tem: '))
d = n/5.81 
arredondado_proximo = math.floor(d)
print(f'Você consegue comprar {arredondado_proximo } dolares')
