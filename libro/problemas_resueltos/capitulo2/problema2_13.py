MAT = int(input("Matricula del estudiante: "))
CARR = str(input("Carrera que cursa: "))
SEM = int(input("Semestre que esta cursando: "))
PROM = float(input("Promedio actual del estudiante: "))
if CARR == 'Economía' or CARR == 'Economia' :
    if SEM >= 6 and PROM >= 8.8 :
        print(MAT)
        print(CARR)
        print("Aceptado")
elif CARR == 'Computación' or CARR == 'Computacion' :
    if SEM > 6 and PROM > 8.5 :
        print(MAT)
        print(CARR)
        print("Aceptado")
elif CARR == 'Contabilidad' or CARR == 'Administración' or CARR == 'Administracion' :
    if SEM > 5 and PROM > 8.5 :
        print(MAT)
        print(CARR)
        print("Aceptado")
print("Fin del programa")
