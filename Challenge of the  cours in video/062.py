# Melhore o desafio 61.perguntando para o usuário se ele quer mostrar mais alguns termos
# O programa encerra quando ele disser que quer mostrar 0 termos
#
print("Gerador de PA")
print("=-=" * 20)
primeiro = int(input("O primeiro termo: "))
razao = int(input("A razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo}-->", end="")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer a mais: "))
print(f"Progressão finalizada em {total} termo")
