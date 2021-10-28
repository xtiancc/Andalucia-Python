from actividad11coche import Coche


def mostrarMenu():
    print("\nMENÚ\n0.- Salir\n1.-Arrancar\n2.-Acelerar\n3.-Frenar\n4.-Detener\n")


print("CONDUCCIÓN COCHE")
print("----------------")

car = Coche()
car.marca = "Toyota"
car.modelo = "Yaris"

op = -1
while(op != 0):

    mostrarMenu()
    op = int(input("Seleccione una opción de la lista: "))

    if (op == 0):
        print("Va a salir del programa")
    elif (op == 1):
        car.arrancar()
    elif(op == 2):
        car.acelerar()
    elif(op == 3):
        car.frenar()
    elif(op == 4):
        car.detener()
    else:
        print("Ha indicado una opción incorrecta.")

print("FIN DEL PROGRAMA")
