#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#caso esteja errado.peça a digitação novamente até ter um valor correto.

while True:
    genero = str(input('Qual e o seu gênero(M/F): ')).upper()
    if genero != M and genero !=F:
        print('Digitação errada, tente novamente')
    else:
        print('informão adquirida')
        break