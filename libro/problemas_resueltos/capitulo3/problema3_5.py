SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
N = int(input("Introduzca un numero entero:"))
for N in range(1, N, 1):
    NUM = int(input("Introduzca una variable tipo entero:"))
    if NUM > 0:
        SUMPOS += NUM
        CUEPOS += 1
    else:
        SUMOTR += NUM
PROGEN = (SUMPOS + SUMOTR) / N
PROPOS = (SUMPOS / CUEPOS)
print(f"Los numeros positivos son: {CUEPOS}")
print(f"El promedio de los numeros positivos es de: {PROPOS}")
print(f"El promedio general de los numeros es de: {PROGEN}")
print("Fin del programa :D")
