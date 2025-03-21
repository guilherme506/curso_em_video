# Faça um programa que calcule a soma entre os
# numeros impares que são múltiplos de três e que
# se encontram no intervalo de 1 até 500
#
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
    print(f"O somatorio de {cont} é {soma}")
