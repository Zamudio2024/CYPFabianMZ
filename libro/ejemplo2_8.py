CATE = int(input("Dame la categoria del empleado:"))
SUE = int(input("Dame el sueldo del trabajador:"))
NSUE = 0
if CATE == 1:
	NSUE = SUE * 1.15
elif CATE == 2:
	NSUE = SUE * 1.10
elif CATE == 3:
	NSUE = SUE * 1.08
elif CATE == 4:
	NSUE = SUE * 1.07
print(f"La categoria a la que pertenece el empleado es {CATE}")
print(f"Su nuevo sueldo sera: {NSUE}")
print("fin del programa")
