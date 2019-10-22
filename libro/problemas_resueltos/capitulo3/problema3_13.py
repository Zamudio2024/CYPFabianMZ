ARSU = 0
ARNO = 0
MERSU = 50000
MES = 0
ARCE = 0
for i in range(0,13,1):
    print(f"Mes: {i}")
    RNO = float(input("Promedio de lluvia caida en la region norte en el mes:"))
    RCE = float(input("Promedio de lluvia caida en la region centro en el mes:"))
    RSU = float(input("Promedio de lluvia caida en la region sur en el mes:"))

    ARNO += RNO
    ARCE += RCE
    ARSU += RSU

    if RSU < MERSU:
        MERSU = RSU
        MES = i
PROCER = ARCE/12
print(f"El promedio de la region centro es: {PROCER} ")
print(f"Mes con menor lluvia en region sur: {MES}")
print(f"Registro del mes con menor lluvia es: {MERSU}")

if ARNO > ARCE:
    if ARNO > ARSU:
        print("La region con mayor lluvia es la norte")
    else:
        print("La region con mayor lluvia es la sur")
elif ARCE > ARSU:
    print("La region con mayor lluvia es el centro")
else:
    print("La region con mayor lluvia es la sur")
print("Fin del progrma :D")
