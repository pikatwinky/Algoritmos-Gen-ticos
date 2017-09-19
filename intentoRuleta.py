import random

elementos = [1, 1, 5, 1, 3]
probabilidades = [0, 0.027, 0.054, 0.729, 0.756, 1]

dardo = random.random()
print(dardo)
elegido = 0

for i in range(len(probabilidades)):
	if dardo < probabilidades[i+1]:
		elegido = elementos[i]
		print(elegido)
		break

		