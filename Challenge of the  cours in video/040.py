# Crie um programa que leia duas notas de um aluno e calcule sua média
# Mostrando uma mensagem no final de acordo com a média atingida:
# - Média abaixo de 5.0: reprovado
# - Média entre 5.0 e 6.9: recuperação
# - média 7.0 ou superior: aprovado

n1 = float(input("primeira nota: "))
n2 = float(input("Segunda nota: "))
m = (n1 + n2) / 2
if m < 5:
    print("Você esta reprovado")
elif m >= 5 or m <= 6.9:
    print("Você esta de recupeção")
elif m >= 7:
    print("Você esta aprovado")
