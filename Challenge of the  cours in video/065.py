# Crie um programa que leia vários números inteiros pelo teclado
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lido
# O programa deve perguntar ao usuário se ele quer ou não quer continuar a digitar valores
lista = []
while True:
    print("=-=" * 20)
    n = int(input("Digite um número: "))
    lista.append(n)
    s = input("Você quer parar(S/N)? ").upper()
    if s == "N":
        continue
    if s == "S":
        print("=-=" * 20)
        print(f"Você digitou {len(lista)} números")
        print(
            f"Entre todos os números digitados o maior é {max(lista)} é o menor é {min(lista)}"
        )
        soma = sum(lista)
        media = soma / len(lista)
        print(f"A média dos números é {media}")
        print("=-=" * 20)
        break
