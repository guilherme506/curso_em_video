#Faça um programa que leia um angulo qualquer e mostre na tela 
#o valor do seno, cosseno e tangente desse angulo
#
from math import (cos,sin,tan,radians,)
x = float(input('Digite um ângulo: '))
n = radians(x)
a = (cos(n))
af = (sin(n))
at = (tan(n))

print(f'As informaçoes obtidas do angulo são:cosseno {a}, seno {af} é a tangente {at} ')
