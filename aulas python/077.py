# Crie um programa que tenha uma tupla com várias palavras(não usar acentos)
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = (
    "peixa",
    "carioca",
    "rei",
    "leao",
    "moana",
    "enrolados",
    "mae",
    "sabe",
    "mais",
    "rapunzel",
    "simba",
    "Gothel",
)
vogais = ('aeiou')
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos: ", end='')
    for letra in p:
        if letra in vogais:
            print(f"{letra.upper()}", end=" ")
