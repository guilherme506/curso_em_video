# Crie um programa que vai gerar cinco números aleatórios e coloque em um tupla
# Depois disso, mostre a listagem de números gerados e também indique o menor é o maior valor que estão na tupla
from random import randint

lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f"Os números sorteados são {lista}")
print(f"O maior número sorteado é {max(lista)}")
print(f"O menor número sorteado é {min(lista)}")
