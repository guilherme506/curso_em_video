# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada individualmente
#
# Usando while
# Repetir até o nome ser 'Joe'
# Listas para armazenar os números pares e ímpares
# Lista para armazenar os números
# Lista para armazenar as tuplas (altura, peso) das pessoas
# Inicializa as variáveis para armazenar o nome e idade da pessoa mais velha
ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar(S/N): ")).upper()
    if resp in "N":
        break
print("-=" * 30)
print(f"{'No.':<4}{'NOME':>10}{'MÉDIA':>8}")
print("-" * 26)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-" * 35)
    opc = int(input("Mostrar notas de qual aluno?(999 interrompe): "))
    if opc == 999:
        print("FINALIZANDO....")
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
print("<<<VOLTE SEMPRE >>>")
