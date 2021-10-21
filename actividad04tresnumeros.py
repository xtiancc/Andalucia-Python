print("MAYOR, MENOR Y SUMA")
print("-------------------")

num1 = int(input("Inserte el primer número: "))
num2 = int(input("Inserte el segundo número: "))
num3 = int(input("Inserte el tercer número: "))
mayor = 0
menor = 0
suma = 0
intermedio = 0

# Número mayor con and
if (num1 >= num2 and num1 >= num3):
    mayor = num1
elif (num2 >= num1 and num2 >= num3):
    mayor = num2
else:
    mayor = num3

# Número menor con and
if (num1 <= num2 and num1 <= num3):
    menor = num1
elif (num2 <= num1 and num2 <= num3):
    menor = num2
else:
    menor = num3

# Suma tres dígitos
suma = num1 + num2 + num3

# Número intermedio
intermedio = suma - mayor - menor

print("El número mayor es " + str(mayor) + " y el número menor es " +
      str(menor) + ". El número intermedio por tanto es " + str(intermedio) + " y la suma de los tres dígitos da " + str(suma))
print("FIN DEL PROGRAMA")
