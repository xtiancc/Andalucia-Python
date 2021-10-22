print("SUMAR DIGIT STRING")
print("------------------")

digitstring = input("Por favor, inserte un número: ")
longitudstring = len(digitstring)
total = 0

for i in range(longitudstring):
    char = digitstring[i]
    digit = int(char)
    total += digit

print("La suma total de los carácteres es: " + str(total))

print("FIN DEL PROGRAMA")
