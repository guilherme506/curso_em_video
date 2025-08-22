# Crie um programa que 4 jogadores joguem um dado(6) e tenham resultados aléatorios. Guarde esses resultados em um dicionário. No final, coloque esses dicionário
# em ordem, savendo que o vencedor tirou o maior número no dado
from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6),
}
ranking = list
print('valores sorteados')
for k,v in jogo.items():
    print(f'{k} tirou o valor {v}.')
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}. ')
    sleep(1)