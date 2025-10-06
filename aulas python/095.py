# Aprimore o DESAFIO 093 apra que ele funcione com, vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
#

time = []
jogador = {}
partida = []
while True:
    jogador.clear()
    jogador["nome"] = str(input("Qual é o nome do jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
    partida.clear()
    for c in range(1, tot + 1):
        partida.append(int(input(f"Quantos gols ele fez na {c}ª partida: ")))
    jogador["gols"] = partida[:]
    jogador["total"] = sum(partida)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]: ')).upper()[0]
        if resp in "SN":
            break
        print('ERROR!, coloque apenas um caractere')
    if resp == "N":
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print("-" * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERROR!!, não existe jogador selecionado com o codico de {busca}!')
    else:
        print(f' ___ LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i , g in enumerate(time[busca]['gols']):
            print(f' No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<<< Volte sempre >>>')