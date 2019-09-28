SUE = float(input("Introduzca su sueldo:"))
if SUE < 1000:
    AUM = SUE * 0.15
    NSUE = SUE + AUM
    print(f"Su nuevo sueldo sera: {NSUE} ")
else:
    AUM = SUE * 0.12
    NSUE = SUE + AUM
    print(f"Su nuevo sueldo sera: {NSUE} ")

print("fin del programa")

