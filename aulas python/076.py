# Crie um programa que tenha uma tupla única com os nomes de produtos e seus respectivos preços na sequência
# No final mostre uma listagem de preços organizando os dados de forma tabular

produtos = (
    "maça",
    40,
    "abacaxi",
    50,
    "pera",
    30,
    "morango",
    10,
    "carambola",
    80,
    "melância", 45,
    "melão", 35,
    "uva", 20,
    "laranja", 80,
    "maracuja", 98,
)
print("=-=" * 13)
print(f'{"TABELA DAS CAIXAS DAS FRUTAS":^40}')
print("=-=" * 13)
for itens in range(0, len(produtos)):
    if itens % 2 == 0:
        print(f'{produtos[itens]:.<30}', end='')
    else: 
        print(f'R${produtos[itens]:>7.2f}')
print("=-=" * 13)