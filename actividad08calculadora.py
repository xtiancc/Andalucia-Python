print("CALCULADORA MATEMÁTICA")
print("----------------------")


def mostrarMenu():
    print("\n0.- SALIR.")
    print("1.- Sumar.")
    print("2.- Restar.")
    print("3.- Dividir.")
    print("4.- Multiplicar.\n")


def sumar(n1, n2):
    return n1 + n2


def restar(n1, n2):
    return n1 - n2


def dividir(n1, n2):
    return n1 / n2


def multiplicar(n1, n2):
    return n1 * n2


op = -1
while(op != 0):

    n1 = int(input("Por favor, inserte el primer dígito: "))
    n2 = int(input("Ahora, inserte el segundo dígito: "))

    valor = ""
    while(valor != "s"):
        mostrarMenu()

        op = int(input("Por favor, indique una acción: "))

        if (op > 0 and op <= 4):
            resultado = 0
            if (op == 1):
                resultado = sumar(n1, n2)
            elif (op == 2):
                resultado = restar(n1, n2)
            elif (op == 3):
                resultado = dividir(n1, n2)
            else:
                resultado = multiplicar(n1, n2)

            print("Resultado: " + str(resultado))
        elif(op > 4 or op < 0):
            print("Debe de seleccionar una acción de las disponibles en el menú.")

        valor = input("¿Desea modificar los números? [S/N]: ")

print("FIN DEL PROGRAMA")
