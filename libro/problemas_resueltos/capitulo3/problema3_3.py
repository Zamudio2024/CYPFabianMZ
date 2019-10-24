SERIE = 0
N = int(input("Introduzca el numero de terminos de la serie:"))
BAND = 'T'
I = 1
for I in range(1, N, 1):
	if BAND == 'T':
		SERIE += 1/I
		BAND = 'F'
	else:
		SERIE -= 1/I
		BAND = 'T'
print(f"El resultado de la serie es: {SERIE}")
print("Fin del programa :D") 
