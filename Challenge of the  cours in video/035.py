# Desenvola um programa que leia o comprimento de três retas
# E diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Valor da primeira reta: '))
r2 = float(input('Valor da segunda reta: '))
r3 = float(input('Valor da terceira reta: '))
if r1+r2>r3 or r1+r3>r2 or r2+r3>r1:
   print('Vocẽ consegue ter um triângulo com essas retas')
else:
    print('você não consegue ter um triângulo com essas')