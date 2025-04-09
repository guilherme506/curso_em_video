#Crie um programa que vai ler vários números e vai colocar-los em uma lista. Depois disso mostre:
#A) Quantos números foram digitados?
#B) A lista dos valores ordenado em forma decrecente
#C) Se o valor 5 foi digitado e está ou não na lista
lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    op = input('Você quer continuar(S/N): ').upper()
    if op == 'S':
        continue
    else:
        break
print(f'A sua lista digitada foi {lista}')
lista.sort(reverse=True)
if 5 in lista:
    print('O número 5 está presente na lista')
else:
    print('O número 5 não está presente na lista')
print(f'A quantidade de números na lista é de {len(lista)}')
print(f'A ordem decrecente da lista é{lista}')