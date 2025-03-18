# Faça um programa que leia o nome completo de uma pessoa 
# Mostrando em seguida a primeira e o último nome separadamente
# Ex: Ana Maria de souza
# Primeiro = Ana 
# Ultimo = Souza

nome = str(input('Qual e o seu nome completo: ')).strip().split()
print(f'O seu primeiro nome é: {nome[0]}')
print(f'O seu ultimo nome é: {(nome[len(nome)-1])}')