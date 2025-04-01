# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA
# mostrando os 10 primeiros termos da progressão usando a estrutura while

print("Gerador de PA")
print("=-=" * 20)

termo = int(input("Primeiro termo: "))
razao = int(input("Valor da razão: "))
cont = 1
while cont <= 10:
    termo = termo + razao
    print(f"{termo} -->", end="")
    cont += 1
print("FIM")
