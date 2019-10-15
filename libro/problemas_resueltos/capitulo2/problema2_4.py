MAT = int(input("Itroduzca la matricula del alumno:"))
CAL1 = float(input("Introduzca su primer calificacion:"))
CAL2 = float(input("Introduzca su segunda calificacion:"))
CAL3 = float(input("Introduzca su tercera calificacion:"))
CAL4 = float(input("Introduzca su cuarta calificacion:"))
CAL5 = float(input("Introduzca su quinta calificacion:"))
PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5)/5
if PRO >= 6:
	print(f"El alumno con matricula {MAT} y promedio {PRO} fue aprobado")
else:
	print(f"El alumno con matricula {MAT} y promedio {PRO} no fue aprobado")
print("Fin del programa")
