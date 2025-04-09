# Desenvolva um programa que que leia quatro valores pelo teclado e guade-os em uma tupla.No final mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares]
tupla = (
    int(input("Digite um número ")),
    int(input("Digite um número ")),
    int(input("Digite um número ")),
    int(input("Digite um número ")),
)
print(f"Você digitou os valores {tupla}")
if tupla.count(9) == 0:
    print("Não existe o número 9 na tupla")
else:
    print(f"A quantidade de vezes que apareceu o número 9 foram {tupla.count(9)}")
if 3 in tupla:
    print(f"A posição em que apareceu o número 3 foi {tupla.index(3) + 1}°posição")
else:
    print("Não existe o número três na tupla")
print('Os valores pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=" ")
