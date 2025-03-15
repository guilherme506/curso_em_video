v = [] # função inicial
z = [] # função após briot
x = [] # multiplicadores
i = 0
k0 = input('Forneça o limitante inferior do intervalo:')
kf = input('Forneça o limitante superior do intervalo:')
x0 = input('Forneça o valor de x0, multiplicador:')
e = input('Forneça a precisão desejada:')
x.append(x0)
briot()
if x0 > kf or x0 < k0:
	print('Forneça um valor dentro do intervalo fornecido!')
	k0 = input('Forneça um novo intervalo inferior:')  
else:
	kf = input('Forneça um novo intervalo superior:')
	a = input('Escolha o primeiro elemento do vetor:')
	b = input('Escolha o segundo elemento do vetor:')
	d = input('Escolha o terceiro elemento do vetor:')
	e = input('Escolha o termo independente da equação:')
	gmax = 3 # o grau maior da equação, quando a equação é de grau menor basta colocar zero como os termos que acompanham x
for i in range(1,2):
	v.append(a)
	v.append(b)
	v.append(d)
	v.append(e)
a1 = v[0] # o valor da equação que desce, mas se mantem sempre o mesmo
def briot():
	for t > e:  
		a2 = a1 * x0 + v[1]
		a3 = a2 * x0 + v[2]
		a4 = a3 * x0 + v[3]
		z.append(a2)
		z.append(a3)
		z.append(a4)
		v = []
		v.append(a1) # v0
		v2 = v[0] * x0 + z[1]
v3 = v[1] * x0 + z[2]
		x[i+1] = x[i-1] - (a[4]/v[3])
		print (x[i+1])
		teste_parada(x[i-1], x[i+1])

    def teste_parada(x[i-1], x[i+1]):
 	
	t = (x[i+1] - x[i-1]) / x
	if t < 0:
		print(-t)
	else:
		print(t)
