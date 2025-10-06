# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler a quantidade de gols feitos em cada partida. No final
# tudo isso será guardado em u  dicionário, incluindo o total de gols feitos durante o campeonato 


jogador = {}
partida = []

jogador['nome'] = str(input('Qual é o nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

for c in range(1, tot + 1):
    partida.append(int(input(f'Quantos gols ele fez na {c}ª partida: ')))
jogador['gols'] =  partida[:]
jogador['total'] = sum(partida)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f' O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["gols"]} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' ===> Na partida {i + 1}°, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')