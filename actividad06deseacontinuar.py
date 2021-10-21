print("¿DESEA CONTINUAR?")
print("-----------------")

respuesta = "s"

while (respuesta.lower() == "s"):

    numero = int(input("Indique un número: "))

    if(numero > 0):
        print("POSITIVO")
    elif (numero < 0):
        print("NEGATIVO")
    else:
        print("CERO")

    respuesta = input("¿Desea continuar? [S / N]: ")
