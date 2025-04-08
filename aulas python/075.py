#Desenvolva um programa que que leia quatro valores pelo teclado e guade-os em uma tupla.No final mostre:
#A) Quantas vezes apareceu o valor 9 
#B) Em que posição foi digitado o primeiro valor 3
#C) Quais foram os números pares 
tot9 = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite outroooo número: '))
n4 = int(input('Aff mais um número: '))
lista = (n1, n2, n3, n4)
if lista == 9 :
    tot9 += 1
print(f'A quantidade de vezes que apareceu o número 9 apareceu foram {tot9}')
print('A posição em que apareceu o número 3 foi {}')
print('Os números que são pares são {}')