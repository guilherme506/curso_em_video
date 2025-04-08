# Crie um tupla com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol, na ordem de colocação depois mostre:
# A) Apenas os 5 primeiros colocados
# B) Os ultimos 4 colocados
# C) Uma lista com os times em ordem alfabetica
# D) Em que posição está o time da chapecoense
times = (
    "Atletico(GO)",
    "Athletico(PR)",
    "Operário(PR)",
    "Crb",
    "Coritiba",
    "Cuiába",
    "Goías",
    "América(MG)    ",
    "Avaí",
    "Novorizontino",
    "Ferroviário(SP)",
    "Remo",
    "Criciúma",
    "Paysandu",
    "Botafogo(SP)",
    "Chapecoense",
    "Amazonas",
    "Vila Nova",
    "Volta Redonda",
    "Athletico(MG)",
)
print(f"Lista dos times da serie B:{times}")
print("=-=" * 20)
print(f"Os primeiros colocados são:{(times[0:5])}")
print("=-=" * 20)
print(f"Os ultimos quatros colocados são:{(times[16:20])}")
print("=-=" * 20)
print(
    f"A colocação do time chapecoense esta em {times.index('Chapecoense') + 1}° posição"
)
print("=-=" * 20)
print(f"O nome dos times em ordem alfabetica:{sorted(times)}")
print("=-=" * 20)
