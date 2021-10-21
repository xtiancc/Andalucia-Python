print("CONJETURA COLLATZ")
print("-----------------")

numero = int(input("Por favor, indique un número: "))

while(numero != 1):
    if(numero % 2 == 0):
        numero = numero / 2
    else:
        numero = numero * 3 + 1
    print(int(numero))

print("FIN DEL PROGRAMA")