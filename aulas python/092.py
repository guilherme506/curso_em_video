# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso o CTPS for diferente de zero,
# O dicionário receberá também o ano de constração e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoas vai se aposentar (35 ANOS).
from datetime import datetime


dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira De Trabalho (0 Não tem): '))
if dados['ctps'] != 0: 
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Sálario R$: '))
    dados['aposentadoria '] = ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')