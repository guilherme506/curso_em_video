# Faça um programa que leia o ano de um nascimento de um jovem
# é intforme de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se ja passou do tempo do alistamento
#
# Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

d = int(input("Em que ano você nasceu: "))
idade = 2025 - d
falta = 18 - idade
passou = idade - 18
if idade <= 17:
    print(
        f"Você ainda não tem idade pra se alistar, daqui a {falta} anos vocẽ precisa-ra se alistar"
    )
elif idade == 8:
    print("Vocẽ ja tem idade pra se alistar")
elif idade > 18:
    print(
        f"Já passou {passou} anos pra se alistar, eu começaria a correr se fosse você"
    )
