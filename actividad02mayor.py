print("NÚMERO MAYOR")
print("------------")

print("Por favor, indique el primer número:")
num1 = int(input())
print("Por favor, indique el segundo número:")
num2 = int(input())

if(num1 > num2):
    print(str(num1) + " es mayor a " + str(num2) + ".")
elif(num1 < num2):
    print(str(num1) + " es menor a " + str(num2) + ".")
else:
    print(str(num1) + " y " + str(num2) + " son iguales.")
print("FIN DEL PROGRAMA.")
