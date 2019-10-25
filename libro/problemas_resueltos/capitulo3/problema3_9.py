SERIE = 0
I = 0
N = int(input("Introduzca un numero entero:"))
for I in range(1, N+ 1, 1):
	SERIE += I**I
print(SERIE)
print("Fin del programa")
