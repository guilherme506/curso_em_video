# Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiro termos
# dessa progressao
#
n1 = int(input("primeiro termo: "))
n2 = int(input("razão da PA: "))
pro = n1 + (11 - 1) * n2
for c in range(n1, pro, n2):
    print(end=f',{c}, ')