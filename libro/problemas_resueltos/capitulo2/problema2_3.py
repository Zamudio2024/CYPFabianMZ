A = float(input("Introduzca la variable de a diferente de 0:"))
B = float(input("Introdzuca la variable de b:"))
C = float(input("Introduzca la variable de c:"))
DIS = B ** 2 - 4 * A * C
print(f"El valor del discriminante es: {DIS}")
if DIS > 0:
	X1 = ((-B) + DIS ** 0.5)/(2*A)
	X2 = ((-B) - DIS ** 0.5)/(2*A)
	print(f"El valor de X1 es: {X1}")
	print(f"El valor de X2 es: {X2}")
print("Fin del programa")
