from math import trunc

print("CALCULO LETRA DNI")
print("-----------------")

aux = input("Por favor, indique su nº de DNI: ")

if (aux.isdigit() is False):
    print("El número de DNI solo puede contener números.")
else:
    # ( nº DNI - (Entero(nº DNI / 23) * 23))
    ndni = int(aux)
    resultado = ndni - (trunc(ndni / 23) * 23)
    cadena = "TRWAGMYFPDXBNJZSQVHLCKET"
    print("La letra de su DNI es " + cadena[resultado] + ".")

print("FIN DEL PROGRAMA")
