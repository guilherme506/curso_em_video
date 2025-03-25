# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
# no final do programa mostre
# - A media de idade do grupo
# - qual é o nome do homem mais velho
# - quantas mulheres tem menos de 20 anos
#
somaidade = 0
mulher = 0
idade_homem = 0
nome_homem = ""
for pess in range(1, 5):
    print(f"____{pess}° pessoa _____")
    nome = str(input("nome: ")).strip().lower()
    idade = int(input("idade: "))
    genero = str(input("gênero(masc,fem): ")).strip().lower()
    somaidade += idade
    if pess == 1 and genero in "masc":
        idade_homem = idade
        nome_homem = nome
    if genero in "masc" and idade > idade_homem:
            idade_homem = idade
            nome_homem = nome

    if genero in 'fem' and idade < 20:
        mulher += 1
media = somaidade/4
print(f"A média da idade do grupo é {media}")
print(f"O nome do homem mais velho é {nome_homem} com a idade de {idade_homem} anos")
print(f"A quantidade de mulher com menos de 20 anos são {mulher}")
