from metodosmath import mostrarMenu, sumar, restar, dividir, multiplicar

print("CALCULADORA MATEMÁTICA")
print("----------------------")

op = -1
while(op != 0):

    mostrarMenu()
    op = int(input("Por favor, indique una acción: "))

    if (op > 0 and op <= 4):

        n1 = int(input("Por favor, inserte el primer dígito: "))
        n2 = int(input("Ahora, inserte el segundo dígito: "))
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

print("FIN DEL PROGRAMA")
