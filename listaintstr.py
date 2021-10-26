def mostrarNombres(nombres):
    print("\nListado:")
    for name in nombres:
        print(name)


print("LISTA NUMEROS Y NOMBRES")
print("-----------------------")

numeros = [20, 14, 55, 99, 77]

print(numeros[0])

numeros.sort()
print("Los numeros ahora están ordenados")

for num in numeros:
    print(num)

nombres = ["Ana", "Adrián", "Lucía", "Carlos", "Pedro", "Heidi", "Ana"]

mostrarNombres(nombres)

nombres.append("El nuevo")
nombres.insert(3, "El del medio")
# nombres.remove("Ana")  # Elimina el primero
nombres.pop(7)

mostrarNombres(nombres)
