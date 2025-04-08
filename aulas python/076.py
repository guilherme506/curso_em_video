#Crie um programa que tenha uma tupla única com os nomes de produtos e seus respectivos preços na sequência
#No final mostre uma listagem de preços organizando os dados de forma tabular

produtos = (('maça',40), ('abacaxi', 50), ('pera', 30), ('morango', 10), ('carambola', 80), ('melância', 45), ('melão', 35), ('uva', 20), ('laranja', 80), ('maracuja', 98))
print('Tabela de valores de caixa de frutas')
print('=-=' * 20)
for tipo, valor in enumerate(sorted(produtos)):
    print(f'{tipo}----------------------------R${valor} reias')