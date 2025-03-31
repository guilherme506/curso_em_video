# O mesmo professor do desafio anterior quer sortear a ordem
# de apresentação de trabalho dos alunos.Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import sample

n1 = input("primeiro aluno: ")
n2 = input("segundo aluno: ")
n3 = input("terceiro aluno: ")
n4 = input("quarto aluno: ")
lista = [n1, n2, n3, n4]
s = sample(lista, k=4)
print(f"a ordem da apresentação do trabalho e{s}")
