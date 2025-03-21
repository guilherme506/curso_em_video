# Faça um programa que leia três números e mostre
# Qual é o maoir e qual é o menor.
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))
if n1 > n2 and n1 > n3 and n2 >= n3:
    print(f"O maior numero é {n1} é o menor numero é {n3}")
elif n1 > n1 and n1 > n3 and n3 >= n2:
    print(f"O maior numero é {n1} é o menor numero é {n2}")
elif n2 > n1 and n2 > n3 and n1 >= n3:
    print(f"O maior numero é {n2} é o menor numero é {n3}")
elif n2 > n1 and n2 > n3 and n3 >= n1:
    print(f"O maior numero é {n2} é o menor numero é {n1}")
elif n3 > n1 and n3 > n2 and n1 >= n2:
    print(f"O maior numero é {n3} é o menor numero é {n2}")
elif n3 > n1 and n3 > n2 and n2 >= n1:
    print(f"O maior numero é {n3} é o menor numero é {n1}")
elif n3 == n1 and n3 == n2 and n2 == n1:
    print("Todos os números são iguais")
