import datetime


def menu():
    print("\n0.- Salir")
    print("1.- Bisiesto")
    print("2.- Narcisista")
    print("3.- Bisiestos vividos\n")


def bisiesto(num):
    if (calculoBisiesto(num)):
        return "Es un año bisiesto."
    else:
        return "El año no es bisiesto."


def narcisista(num):
    aux = str(num)
    resultado = 0

    for i in range(len(aux)):
        resultado += int(aux[i]) ** int(len(aux))

    if (resultado == num):
        return "Este número es narcisista."
    else:
        return "Este número no es narcisista."


def listado(num):
    fecha = datetime.date.today()
    total = 0
    for i in range(num, fecha.year):
        if (calculoBisiesto(i)):
            print(i)
            total += 1

    return "\nTotal de años bisiestos: " + str(total)


def calculoBisiesto(num):
    if (num % 4 == 0 and (num % 100 != 0 or (num % 100 == 0 and num % 400 == 0))):
        return True
    else:
        return False


def comprobarNum(num):
    if (num.isdigit()):
        return True
    else:
        return False
