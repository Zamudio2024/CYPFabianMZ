# print tiene 4 formas de uso
"""
1.- con comas
2.- con signo '+'
3.- con la funcion fromat()
4.- es con una variante de format ()
"""
#Con comas , concatenar agregando
# un espacion y haciendo casting de tipo.
edad = 18
nombre = "Fabian"
estatura = 1.75
print (edad , estatura , nombre)
#con '+' hace lo mismo pero no realiza el casting automático
#no agrega espacio
print(str(edad) + str(estatura) + nombre)
# funcion format()
print("Nombre: {} Edad: {} Estatura {} ".format(nombre, edad, estatura))

#con una variante de format () simplificada
print(f"Nombre: \"{nombre}\" \nEdad: \t{edad} \nEstatura: \t{estatura}")

#print y el argumento end
print("Solo hay 10 tipos de personas, las que saben binario y las que no", end="---")
print("Otra linea")
