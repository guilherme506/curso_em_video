#Faça um programa que leia a largura e a altura de uma parede em metros
#calcule a sua área e a quantidade de tinta necessária para pintá-la
#sabendo que cada litro de tinda pinta uma aŕea de 2m²
import math
l = float(input('largura da parede em metros: '))
# l = largura
a = float(input('Altura da parede em metros: '))
# a = altura
ar = a * l 
# ar = area
t = ar/2
# t = quantida de tinta
print(f'A area da parede e de {ar} metros quadrados é a quantidade de tinta necéssaria pra pintar ela e de {t} litros')