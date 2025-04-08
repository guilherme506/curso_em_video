# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 a 20) e mostrá-lo por extenso.
numeros = (
    "Zero",
    "Um",
    "Dois",
    "Três",
    "Quatro",
    "Cinco",
    "Seis",
    "Sete",
    "Oito",
    "Nove",
    "Dezonze",
    "Doze",
    "Treze",
    "Catorze",
    "Duinze",
    "Dezesseis",
    "Dezessete",
    "Dezoito",
    "Dezenove",
    "Vinte",
)
while True:
    n = int(input("Digite um número de (0 a 20): "))
    if n <= 20 and n >= 0:
        print(f"Você digitou o número {numeros[n]}")
        break
    else:
        print("Esse número não é uma opção, tente novamente")
