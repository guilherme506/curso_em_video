valores = []
for cont in range(0, 4):
    valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c}, se escontra o valor {v}!')
print('Chegamos no final da lista')
b = valores[:]#cria uma copia de valores dentro do b 
b[2] = 8