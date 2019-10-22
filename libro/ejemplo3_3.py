CUECER =0
N = int(input("Dame un numero entero positivo:"))
for i in range(0, N, 1):
    NUM = int(input("Ingresa un numero entero:"))
    if NUM ==0:
        CUECER +=1
print("El numero de 0's capturados fue:", CUECER)
