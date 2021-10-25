from actividad09metodobn import *

print("AÑO BISIESTO / Nº NARCISISTA")
print("----------------------------")

op = -1
while (op != 0):

    menu()
    op = input("Por favor, indique una opción del menú: ")

    if (comprobarNum(op)):
        opaux = int(op)
        if (opaux == 0):
            print("Va a salir del programa.")
        elif (opaux < 0 or opaux > 3):
            print("No ha seleccionado una opción correcta.")
        else:
            num = input("Indique un número: ")

            if(comprobarNum(num)):
                numaux = int(num)
                if(numaux == 1):
                    resultado = bisiesto(numaux)
                elif(numaux == 2):
                    resultado = narcisista(numaux)
                else:
                    resultado = listado(numaux)

                print(resultado)
            else:
                print("Solamente está permitido incluir números.")
    else:
        print("No ha seleccionado una opción correcta.")

print("FIN DEL PROGRAMA")

input("Pulse cualquier tecla para salir: ")
