print("NÚMEROS PARES")
print("-------------")

inicio = int(input("Indique el digito de inicio: "))
fin = int(input("Indique el digito final: "))

for i in range(inicio, fin + 1):
    if (i % 2 == 0):
        print(i)

print("FIN DEL PROGRAMA")