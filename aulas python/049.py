# Refaça o desafio 009, mostrando a tabuada de
# um número que o usuário escolher, só que agora
# utlizando um laço for
#
n = int(input("Digite um numero: "))
for c in range(1, 11):
    print(f"{n} vezes {c} e igual {n * c}")
