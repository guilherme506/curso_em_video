# Crie um programa, onde o usuário possa digitar cinco valores e cadastre-os em uma list.
# Já na posição correta de inserção(sem usar o sort)
# No final, mostre os números a lista ordenada na tela
lista = []
for ord in range(5):
    num = int(input("Digite um número: "))
    if ord == 0 or num > lista[len(lista) - 1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print("===" * 30)
print(f"Os valor da sua lista são {lista}")
