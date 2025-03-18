# Crie um programa que leia o nome de uma pessoa 
# E diga se ela tem "silva" no nome 

n = str(input('Qual é o seu nome completo: '))
f = 'silva' in n
print (f'Você tem o sobrenome silva:{f}')