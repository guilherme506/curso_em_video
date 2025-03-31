# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
import math

n = float(input("digite um numero: "))
n1 = n * 2
n2 = n * 3
n3 = math.sqrt(n)
print(
    f"O dobro do valor do número é {n1}, o triplo é {n2} é a raiz quadrada do número é {n3}"
)
