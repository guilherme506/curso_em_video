# Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras minusculas  e minuscuslo
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome

frase = str(input("Qual é o seu nome completo? "))

# f.lower(n)  colocar tudo em minusculo

# analise = len(f)
# analise = f.split
# f.stip(n) remover os espaços inuteis

# f.split(n) vai separar cada palavra
print(f"O seu nome com todo minusculo fica {frase.lower()}")
print(f"O seu nome com todo maiusculo fica {frase.upper()}")
dividido = frase.split()
print(f"A quantidade de letras no seu nome e de {len('-'.join(dividido))}")
print(f"a quantidade de letras do seu primeiro nome e de {len(dividido[0])}")
