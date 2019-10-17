SUE = float(input("Introduzca el sueldo basico del trabajador:"))
CATE = int(input("Introduzca la categoria del trabajador (1-4):"))
HE = int(input("Introduzca las horas extras que trabajo:"))
if CATE == 1:
	PHE = 30
elif CATE == 2:
	PHE = 38
elif CATE == 3:
	PHE = 50
elif CATE == 4:
	PHE = 70
else:
	PHE = 0
if HE > 30:
	NSUE = SUE + 30*PHE
else:
	NSUE = SUE + HE*PHE
print(f"El nuevo sueldo sera: {NSUE}")
print("Fin del programa :D")
