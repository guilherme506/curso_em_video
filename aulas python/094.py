# Crie um programa que leia nome, sexo e idade de várias pessoas , guardando os dados de cada pessoa em um dicionário em uma lista
# No final, mostre:
# A) Quantas pessoas foram cadastradas 
# B) A média de idade do grupo 
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média 

galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('Genero(M/F): ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERROR!!, digite apenas um caracter')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resp = str(input('quer continuar?[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERROR, Coloque apenas um caracter')
    if resp == 'N':
        break       
print(f'Ao todo temos no total {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'Á media de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()
print('Pessoas com idade acima da média: ', end='')
for p in galera: 
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< Encerrado >>')