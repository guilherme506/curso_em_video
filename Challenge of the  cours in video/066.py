# Crie um programa que leia vários números inteiros pelo teclado.
# O programa vai parar quando o usuário digitar o valor 999, que é a condição de parada
# No final mostre quantos números foram digitados e qual foi a soma entre eles
# Ignore a flag
soma = 0
quant = 0
while True:
    n = int(input("Digite um número(caso queire parar coloque o número 999): "))
    if n != 999:
        soma += n
        quant += 1
    elif n == 999:
        print(f"O resultado da soma dos seus numeros é {soma}")
        print(f"A quantidade de números digitados é {quant}")
        break
