# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
# No final, mostre qual e o maior é o menor valor, e suas respectivas posições na lista
lista = []
for valor in range(5):
    lista.append(int(input("Digite um número: ")))
print(f"A lista digitada foi {lista}")
print(
    f"O maior valor da lista é {max(lista)} é a sua posição é {lista.index(max(lista)) + 1}"
)
print(
    f"O menor valor da lista é {min(lista)} é a sua posição é {lista.index(min(lista)) + 1}"
)
