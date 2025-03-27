# Crie um programa que leia dois valores e mostre um menu na tela:
# [somar]
# [multiplicar]
# [maior]
# [novos números]
# [sair do programa]
# Seu programa deverá realizar a operação solicitada em cada caso
n1 = int(input("Escolha um número: "))
n2 = int(input("Escolha outro número: "))
opçao = 0
while opçao != 5:
    print("""
         [1] - somar
         [2] - Multiplicar
         [3] - maior
         [4] - Novos números
         [5] - Sair do Programa
         """)
    opçao = int(input('Qual é a sua opção: '))
    if opçao == 1:
        print(f"A soma do valor {n1} e {n2} é {n1 + n2}")
    elif opçao == 2:
        print(f"A multiplicação de {n1} e {n2} é {n1 * n2}")
    elif opçao == 3:
        if n1>n2:
            print(f"O maior valor é {n1}")
        else:
            print(f'O maior valor é {n2}')
    elif opçao == 4:
        n1 = int(input("Escolha um número: "))
        n2 = int(input("Escolha outro número: "))
    elif opçao == 5:
        print('fim do programa')
    elif opçao > 5:
        print('não tem essa opção, tente novamente')
    print('=-=' * 10)
