# A confederação nacional de natação precisa de um programa
# que leia o ano de nascimento de um atleta  e mostre
# sua categoria, de acordo com a idade
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 20 Anos: Sênior
# - Acima: Master

ano = int(input("Em que ano você nasceu: "))
idade = 2025 - ano
if idade <= 9:
    print("Você e um atleta nível Mirim")
elif idade >= 10 and idade <= 14:
    print("Você e um atleta Infantil")
elif idade >= 15 and idade <= 19:
    print("Você e um atleta Junior")
elif idade == 20:
    print("Você e um atleta Sênior")
elif idade > 20:
    print("Você e um atleta Master")
