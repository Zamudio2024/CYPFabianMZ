P = int(input("Introduzca un numero entero:"))
Q = int(input("Introduzca otro numero entero:"))
EXP = P**3 + Q**4-2*P**2
if EXP < 680:
	print(f"El resultado de P y Q es {EXP}")
	print(P)
	print(Q)
print("Fin del programa")
