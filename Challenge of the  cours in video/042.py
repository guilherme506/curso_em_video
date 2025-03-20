# Refaça o DESAFIO 35 dos triangulos.
# acrescentando o recurso de mostrar que tipo de triângilo sera formado
# - Equilátero: todos os lados iguais
# - isósceles: dois lados iguais
# - escaleno: todos os lados diferentes

r1 = float(input('primeira reta:'))
r2 = float(input('segunda reta:'))
r3 = float(input('terceira reta:'))
if r1 +r2 <= r3 or r2 + r3 <= r1 or r1 + r3 <= r2:
    print('Isso não e um triãngulo')
elif r1 == r2 and r3 == r1 and r2 == r3:
    print('Você adquiriu um triângulo Equilátero ')
elif r1 == r2 and r1 != r3 and r2 != r3:
    print('Você adquiriu um triângulo Isósceles')
elif r1 != r2 and r2 != r3 and  r1 != r3:
    print('Você adquiriu um triânfulo Escaleno')