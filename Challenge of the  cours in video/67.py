# Faça um programa que mostre a tabuada de vários números,um de cada vez,para cada valor digitado pelo usuário.
# o programa será interrompido quando o número solicitado for negativo

while True:
    n = int(input('Digite um número pra descobrir a tabuada: '))
    if n > 0 :
        for c in range (11):
            print(f'{n}  vezes {c} e igual {n*c}')
    else:        
        print('obrigado, fim do programa')
        break