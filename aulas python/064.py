# Crie um programa que leia que leia vários números inteiros pelo teclado
# O programa só vai parar quando o usuário digitar o valor 999.
# que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles
# desconsiderando o flag
soma = 0
numeros = 0
while True:
    n = int(input("Digite um numero "))
    if n != 999:
        soma += n
        numeros += 1
    elif n == 999:
        print(f"Você digitou {numeros} números ")
        print(f"A soma dos valores de todos os números é {soma}")
