# Crie um programa que leia o nome e o preço de várias produtos
# O programa deverá perguntar se o usuário vai continuar.
# No final mostre:
# A)Qual é o total gasto na compra
# B)Quantos produtos custam mais de R$1000
# C)Qual é o nome do produto mais barato
total = totmil = menor = cont = 0
barato = ''
while True:
    print('LOJA DO JOÃO')
    produto = str(input("Digite o nome do produto: "))
    preço = float(input("Digite o preço do produto: "))
    print('=-=' * 20)
    cont += 1
    total += preço
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    if preço > 1000:
        totmil += 1
    resp = ' '
    while resp not in 'SN': 
        resp = input("Gostaria de adicionar mais produtos(S/N): ").upper().strip()[0]
    if resp == 'N':
        break
print(f"O preço gasto da compra é de R${total:1f}")
print(f"Vocẽ tem {totmil} produtos acima de 1000 reais")
print(f"O produto mais barato foi {barato} que custou {menor:1f} reais")
