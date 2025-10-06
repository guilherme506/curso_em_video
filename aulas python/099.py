#faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu progresso tem que analisar todos os valores qual deles é maior .
from time import sleep
def maior(*num):
    m = max(num)
    quant = len(num)
    print('Analisando valores... ', flush=True)
    for c in num:
        print(f'{c} ', end='', flush=True)
        sleep(0.5)
    print(f'Ao todo temos {quant}')
    print(f'O maior numero é {m}')
    print('-=' * 20)
#codigo príncipal
maior(7, 8 , 6 ,3 , 4, 44)  
maior(4, 5 ,8)
maior(1, 0 , 9)
maior(1, 7)