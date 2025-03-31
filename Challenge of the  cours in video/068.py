# Faça um programa que jogue par ou impar com o computador.
# o jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivvas que ele conquitou no final do jogo
from random import randint

while True:
    print(
        "escolha sua jogada: ",
    )
    print("=-=" * 20)
    n = int(input("Qual número você irá jogar(0 a 10): "))
    c1 = randint(0, 10)
    soma = c1 + n
    vit = 0
    j = int(
        input("""
    1 - impar
    2 - par 
    insira o número: """)
    )
    if n > 10:
        print("O número e muito mais alto do que o pedido, adeus")
        break
    elif n < 0:
        print("não aceitamos números negativo, adeus")
        break
        print("=-=" * 20)
    elif soma % 2 == 0:
        if j == 2:
            print(f"Você ganhou, pelo menos isso você consegue {c1}")
            vit += 1
        elif j == 1:
            break
    elif soma % 2 != 0:
        if j == 1:
            print(f"Você ganhou, pelo moneos isso você consegue {c1}")
            vit += 1
        elif j == 2:
            break
print("=_=" * 20)
print(f"{soma}m,{c1}")
if vit == 0:
    print(
        "O jogo acabou, você teve 0 vitórias consecutivas.Eu não pensei que você seria tão ruim, eu teria até pena, mas como eu sou um robô eu não ligo"
    )
elif vit < 5 and vit <= 1:
    print(
        "O jogo acabou, você teve {vit} vitórias consecutivas.Vai embora enquanto está ganhando xo."
    )
elif vit > 5:
    print("o jogo acabou, você teve {vit} vitóias consecutivas.Vai embora seu chato")
