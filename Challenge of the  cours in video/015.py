#Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado
#calcule o preço a pagar, sabendo que o carro custa 60 reias por dia e 0.15 por km rodado

k = float(input('quantos km o carro percorreu: '))
# k = km percorrido
d = float(input('Quantos dias o carro foi alugado: '))
# d = dias alugados do carro

pd = d * 60 
pk = k * 0.15

print(f'O valor do aluguel do carro é {pd} reais e o valor do km rodado e de {pk} reais')
