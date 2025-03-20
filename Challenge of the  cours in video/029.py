#escreva um programa que leia a velociade de um carro
#
#se ele tiver ultrapassado 80km/h. Mostre uma mensagem dizendo que eles foi multado 
#
#A multa vai custar R$:7,00 por cada km acima do limite.
#
velocidade = int(input('Velocidade do carro: '))
numero = 80
multa = (velocidade - numero)*7
if velocidade <= numero:
    print('parabens você não foi multado')
else:
    print(f"Parabens você foi multado por excesso de velociade o valor da multa e de {multa} reais")