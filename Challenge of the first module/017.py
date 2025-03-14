#faça um programa que leia o comprimento do cateto 
#oposto e do cateto adjacente de um triangulo retangulo 
#calcule e mostre o comprimento da hipotenusa

from math import (sqrt)

ca = float(input('escreva o numero do cateto adjacente: '))
co = float(input('escreva o numero do cateto oposto: '))
h = (ca**2)+(co**2)
print(f'A hipotenusa do triangulo e {sqrt(h)}')