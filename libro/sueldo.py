sueldos= []
suma = 0
for indice in range(7):
    sueldos.append(int(input("Sueldos:")))
print(sueldos)

for indice in range (7):
    suma += sueldos[indice]
promedio = suma / 7
print(f"El promedio de sueldos es: {promedio}")
cont = 0
for indice in range(7):
    if sueldos[indice] > promedio:
        cont += 1
        print(f"Arriba: {sueldos[indice]}")
