from math import trunc

print("CALCULADORA DÍA DE NACIMIENTO DE SEMANA")
print("---------------------------------------")

dia = int(input("Por favor, indique el día de nacimiento: "))
mes = int(input("Por favor, indique el mes de nacimiento: "))
ano = int(input("Por favor, inidque su año de nacimiento: "))

if (mes == 1):
    mes = 13
    ano = ano - 1
elif (mes == 2):
    mes = 14
    ano = ano - 1

# 1
calculo1 = trunc(((mes + 1) * 3) / 5)

# 2
calculo2 = trunc(ano / 4)

# 3
calculo3 = trunc(ano / 100)

# 4
calculo4 = trunc(ano / 400)

# 5
calculo5 = trunc(dia + (mes * 2) + ano + calculo1 +
                 calculo2 - calculo3 + calculo4 + 2)

# 6
calculo6 = trunc(calculo5 / 7)

# 7
resultado = trunc(calculo5 - (calculo6 * 7))

# 8
if (resultado == 0):
    print("Sábado")
elif (resultado == 1):
    print("Domingo")
elif (resultado == 2):
    print("Lunes")
elif (resultado == 3):
    print("Martes")
elif (resultado == 4):
    print("Miércoles")
elif (resultado == 5):
    print("Jueves")
elif (resultado == 6):
    print("Viernes")
# 9
