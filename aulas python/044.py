# Elabore um programa que calcule o valor a ser pago por um produto
# Considerando o seu preço normal e condição de pagamento:
# Á vista dinherio/cheque: 10% de desconto
# Á vista no cartão: 5% de desconto
# Em ate 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
#
p = float(input("Qual é o valor da sua compra: "))
f = input("""Qual sera a forma de pagamento
          1 - dinheiro/cheque
          2 - cartão á vista
          3 - cartão 2x
          4 - cartão 3x ou mais 
          opçao:  """)
op1 = p - (p * (10 / 100))
op2 = p - (p * (5 / 100))
op3 = p
op4 = p + (p * (20 / 100))
if f == "1":
    print(f"O valor a ser pago e de {op1}")
elif f == "2":
    print(f"O valor a ser pago e de {op2}")
elif f == "3":
    print(f"O valor a ser pago e de {op3}")
elif f == "4":
    print(f"O valor a ser pago e de {op4}")
