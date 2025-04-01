# Escreva um programa que pergunta o salário de um funcionário e calcule
# o valor do seu aumento
#
# Para salarios superiores a R$1250,00, calcule um aumento de 10%
#
# Para os inferiores ou iguais o aumento é de 15%
n = float(input("Qual é o seu salário: "))
s1 = n * (10 / 100)
s2 = s1 + n
p1 = n * (15 / 100)
p2 = p1 + n
if n > 1250:
    print(f"O valor do seu salário com o aumento ficou {s2}")
elif 0 < n < 1250:
    print(f"O valor do seu salário com o aumento ficou {p2}")
else:
    print("Você não tem um salário, vai trabalhar vagabundo")
