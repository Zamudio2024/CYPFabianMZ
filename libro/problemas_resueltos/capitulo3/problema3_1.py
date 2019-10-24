SUMPAR = 0
SUMIMP = 0
CUEPAR = 0
PROPAR = 0
I = 1
for I in range(0,271,1):
	NUM = int(input("Introduce un numero entero:"))
	if NUM != 0:
		if (-1 ** NUM) > 0:
			SUMPAR += NUM
			CUEPAR +=1
		else:
			SUMIMP += NUM
	I +=1
PROPAR = SUMPAR / CUEPAR
print(f"El promedio de los numeros es:{PROPAR}")
print(f"La suma de los impares es:{SUMPAR}")
print("Fin del programa :D")
