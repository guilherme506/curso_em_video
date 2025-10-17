# Crie um programa que tenha uma função() chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa.
# Retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obriagatorio nas eleições.
from datetime import date
def voto(ano,):
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f'com {idade} anos: Nâo vota'
    elif idade > 18:
        return f'Com {idade} anos: Voto obrigatorio '
    elif idade >= 65:
        return f'Com {idade} anos: Voto Opcional'


nasc = int(input('Em que ano você nasceu: '))
print(voto(nasc))