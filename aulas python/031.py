# Desenvolva um programa que pergunta a distância de uma viagem em km
# Calcule o preço da passagem, cobrando R$0,50 por km para viagem de ate 200 km
# e R$0,45 para viagens mais longas.
#
d = int(input("Qual é a distância da viagem em km: "))
c = d * 0.50
l = d * 0.45
if d <= 200:
    print(f"O valor da viagem e de {c}")
else:
    print(f"O valor da viagem e de {l}")
