TIPOENF = int(input("Tipo de enfermedad del paciente (1-4): "))
EDAD = int(input("Edad del paciente: "))
DIAS = int(input("Dias de hospitalizacion:"))
COSTOT = 0
if TIPOENF == 1 :
    COSTOT = DIAS * 25
elif TIPOENF == 2 :
    COSTOT = DIAS * 16
elif TIPOENF == 3 :
    COSTOT = DIAS * 20
elif TIPOENF == 4 :
    COSTOT = DIAS * 32

if EDAD >= 14 and EDAD <= 22 :
    COSTOT *= 1.1
print(f"El costo total del paciente es : {COSTOT}")
print("Fin del programa :D")
