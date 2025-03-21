# Escreva um programa que leia dois números inteiros
# e compare-os, mostrando na tela uma mensagem
# - O primeiro valor e maior
# - o segundo valor é maior
# - Não existe valor maior, os dois são iguais
n1 = int(input("Escreva um número inteiro: "))
n2 = int(input("Escreva outro número inteiro: "))
if n1 > n2:
    print(f"O primeiro valor é maior, é o segundo valor é maior que {n2 - 1} ")
elif n2 > n1:
    print(f"O primeiro valor é maior, é o segundo valor é maior que {n1 - 1}")
else:
    print("Não existe valor maior, os dois são iguais")
