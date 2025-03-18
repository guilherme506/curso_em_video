#Um professor quer sortear um dos seus quatro alunos 
#para apagar o quadro.Faça um programa que ajude ele
#lendo o nome deles e escrevendo o nome do escolhido

from random import(choice)
n1 = (input('primeiro aluno: '))
n2 = (input('segundo aluno: '))
n3 = (input('terceiro aluno: '))
n4 = (input('quarto aluno: '))
list = (n1,n2,n3,n4)
s = choice(list)
print(f'Meus parabéns {s} você foi o sortudo de apagar o quadro')