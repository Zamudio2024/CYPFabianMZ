NOM = 0
SUE = float(input("Introduzca el sueldo:"))
while SUE != -1:
	if SUE < 1000:
		NSUE = SUE * 1.15
	else:
		NSUE = SUE * 1.12
	NOM += NSUE
	print(f"El nuevo sueldo sera: {NSUE}")
	SUE = float(input("Indroduzca el siguiente sueldo:"))
print(f"La nomina es de: {NOM}")
print(f"Fin del programa :D")
