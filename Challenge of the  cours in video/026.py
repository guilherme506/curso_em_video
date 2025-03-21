# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez
n = str(input("digite uma frase: ")).upper().strip()
print(f"Ao analisarmos a frase {n}, obtivemos os seguintes caracteres: ")
print(f"A quantide de letras A encontradas foram de: {n.count('A')} vezes na frase")
print(f"A primeira vez que a letra A aparece é: {n.find('A') + 1}")
print(f"A ultima vez que a letra A aparece é: {n.rfind('A') + 1}")
