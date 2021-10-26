def mostrarDoble():
    try:
        num = int(input("Introduzca un número: "))
        print("El doble es: " + str(num*2))
    except ValueError:
        print("Error, debes introducir un número.")
        mostrarDoble()


print("CONTROL DE ERRORES")
print("------------------")

mostrarDoble()
