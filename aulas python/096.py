#Faça um programa que tenha uma função chamado Área(). que recceba as dimensões de um terreno retangular(Largura e comprimento) e  mostre a área do terreno.
def Área (l, c):
    a = l * c
    print(f'A área do retangulo é {l} * {c} = {a}')


print('CONTROLE DE TERRENOS')
print('-' * 30)
Área(
l = float(input('Largura: ')),
c = float(input('Comprimento: '))
)
