edad = int(input("Que edad tienes?:"))
INE = bool(int(input("Tienes INE? (0 NO / 1 SI):")))
if edad >= 18 and INE == True:
    print("Es mayor de edad")
    print("Puedes entrar al bar")
print("fin de programa")

