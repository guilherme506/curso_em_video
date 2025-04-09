# Crie um programa onde o usuário digite uma expressão qualquer que use parêntese
# Seu aplicativo deverá analisar se a expressão passada está com o parêntese abertos ou fechados na ordem correta 
lista = []
ex = str(input('Digite uma expressão: '))
for simb in ex:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada!')
