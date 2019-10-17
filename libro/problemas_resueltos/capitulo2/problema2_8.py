COMPRA = float(input("Introduzca el monto de la compra:"))
if COMPRA < 500:
	pagar = COMPRA
else:
	if COMPRA <= 1000:
		pagar = COMPRA - (COMPRA * 0.05)
	else:
		if COMPRA <= 7000:
			pagar = COMPRA - (COMPRA * 0.11)
		else:
			if COMPRA <= 15000:
				pagar = COMPRA - (COMPRA * 0.18)
			else:
				pagar = COMPRA - (COMPRA * 0.25)
print(f"El total a pagar es: {pagar}")
print("Fin del programa")
