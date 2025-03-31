# Faça um algoritmo que leia o salàrio de um funcionário
# e mostre seu novo salário com 15% de aumento

n = float(input("valor do salário: "))
n1 = n * (15 / 100)
s = n + n1
print(f"O valor do salário do funcionário com o aumento ficou em {s}")
