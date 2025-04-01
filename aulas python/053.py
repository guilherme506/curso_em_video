# Crie um programa que leia uma frase qualquer e diga
# se ela é um políndromo, desconsiderando os espaços
#
n = str(input("Escreva uma frase: ")).lower().strip()
frase = n.split()
junto = "".join(frase)
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print(f' O inverso de {junto} é {inverso}')
if inverso == junto:
    print("A sua frase é um políndromo")
else:
    print("A sua frase não é um políndromo")
