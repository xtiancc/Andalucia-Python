print("LISTADO NOMBRES")
print("---------------")


def ejecutar():

    lista = []

    while(True):

        nombre = input("\nIndique un nombre:")

        if (nombre.isalpha()):
            lista.append(nombre)

            print()
            longitud = len(lista)
            for i in range(longitud):
                nombre = lista[i]
                print(str(i) + ".-" + nombre)

            if(lista[-1] == "OK"):
                break
        else:
            print("Parece que " + nombre + " no es un nombre. ")

    op = -1
    while(op != 0):

        print("\nMENÚ")
        print("----")
        print("0.- Salir")
        print("1.- Nuevo nombre")
        print("2.- Eliminar nombre")
        print("3.- Comenzar de nuevo\n")

        op = input("Seleccione una opción del menú: ")
        print("")

        if(op.isdigit()):

            opaux = int(op)

            if (opaux == 0):
                print("Va a salir del programa.")

            elif(opaux == 1):

                name = input("Seleccione nombre a agregar: ")
                lista.append(name)
                print("Se ha agregado " + name + " a la lista.\n")

                longitud = len(lista)
                for i in range(longitud):
                    nombre = lista[i]
                    print(str(i) + ".-" + nombre)

            elif(opaux == 2):

                position = int(input("Seleccione posición a eliminar: "))

                print("Se va a eliminar " +
                      lista[position] + " de la lista.\n")
                lista.pop(position)

                longitud = len(lista)
                for i in range(longitud):
                    nombre = lista[i]
                    print(str(i) + ".-" + nombre)

            elif(opaux == 3):
                ejecutar()

            else:
                print("Parece que ha indicado una opción incorrecta.")

        else:
            print("Parece que ha indicado una opción incorrecta.")


ejecutar()

print("FIN DEL PROGRAMA")
