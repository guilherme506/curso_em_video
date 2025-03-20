# Faça um programa um ano qualquer e mostre se ele é um ano bissexto

ano = int(input('Em que ano estamos: '))
if ano % 4 == 0 and ano % 100 !=0:
    print('O ano em que você se encontra e bissexto')
else:
    print('O ano em que você se encontra não e bissexto')