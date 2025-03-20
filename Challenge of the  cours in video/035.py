# Desenvola um programa que leia o comprimento de três retas
# E diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Valor do primeira segmento: '))
r2 = float(input('Valor do segunda segmento: '))
r3 = float(input('Valor do terceira segmento: '))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
   print('Vocẽ consegue ter um triângulo com essas retas')
else:
    print('você não consegue ter um triângulo com essas')