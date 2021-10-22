print("VALIDACIÓN DE ISBN")
print("------------------")

aux = input("Por favor, introduzca ISBN: ")
calculo = 0

if ((aux.isdigit() is False or len(aux) != 10)):
    print("El ISBN es incorrecto.")
else:
    for i in range(10):
        calculo += int(aux[i]) * (i + 1)
    print(str(calculo))

    if (calculo % 11 == 0):
        print("El ISBN es correcto.")
    else:
        print("El ISBN es incorrecto")

print("FIN DEL PROGRAMA")
