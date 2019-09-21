L1 = float(input("Introduzca la distancia de L1:"))
L2 = float(input("Introduzca la distancia de L2:"))
L3 = float(input("Introduzca la distancia de L3:"))
S = (L1 + L2 + L3) / 2
AREA = (S * (S - L1) * (S - L2) * (S - L3)) ** 0.5
print(f"El area del trianguo es: {AREA}")
