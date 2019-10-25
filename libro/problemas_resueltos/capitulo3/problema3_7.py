GRA = 0
MED = 0
CHI = 0
N = int(input("Introduzca un numero entero:"))
for N in range(1, N, 1):
	V = float(input("Introduzca un numero real:"))
	if V <= 200:
		CHI += 1
	elif V < 400:
		MED += 1
	else:
		GRA += 1
print(f"Las ventas menores a 200 fueron: {CHI}")
print(f"Las ventas entre 200 y 400 fueron: {MED}")
print(f"Las ventas mayores a 400 fueron: {GRA}")
print("Fin del programa :D")
