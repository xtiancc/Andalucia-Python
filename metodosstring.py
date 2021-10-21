print("MÉTODOS STRING")
print("--------------")

cadena = "primero python"

# Métodos de String
print(cadena.lower())
print(cadena.replace("o", "0"))
print(cadena[0])
print(len(cadena))  # Debe ser string cuando se concatena
print(cadena.find("P"))  # Devuelve error puesto que no hay P mayúsculas
print(cadena.find("p"))
print(cadena.find("p", 1))  # Contabiliza a partir de "rimero python"
print(cadena.startswith("A"))
print(cadena.endswith("n"))
print(cadena.isdigit())
print(cadena.isalpha())
print(cadena[2:])

print("FIN DEL PROGRAMA")
