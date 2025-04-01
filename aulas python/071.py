# Crie um programa que simule o funcionamento de um caixa eletrônico +
# No início, pergunte qual será o valor a ser sacado(número inteiro)
# e o programa vai informa quantas cédulas de cada valor serão entregues
# OBS:Considere que o caixa possui cédulas de R$ 50, R$20, R$10 e R$1
print("Bom dia caro cliente, notas disponíveis:R$ 50, R$20, R$10 é R$1")
valor = int(input("Qual sera o valor sacado: "))
cinco = round(valor // 50)
vinte = round((valor - (50 * cinco)) // 20)
dez = round((valor - (cinco * 50) - (20 * vinte)) // 10)
um = round((valor - (50 * cinco) - (20 * vinte) - (10 * dez)) // 1)
print(f"A quantidade de notas recebidas de R$50 são {cinco}")
print(f"A quantidade de notas recebidas de R$20 são {vinte}")
print(f"A quantidaed de notas recebidas de R$10 são {dez}")
print(f"A quantidade de notas recebidas de R$1 são {um}")
