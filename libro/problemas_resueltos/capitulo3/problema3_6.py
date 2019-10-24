MAY = -100000
MEN = 100000
N = int(input("Introduce un numero entero:"))
for N in range(1, N, 1):
		NUM = int(input("Introduzca una variable tipo entero:"))
		if NUM > MAY:
				MAY = NUM
		elif NUM < MEN:
				MEN = NUM
print(f"El numero mayor es: {MAY}")
print(f"El numero menor es: {MEN}")
print("Fin del programa :D")
