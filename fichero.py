print("EJEMPLO FICHERO")
print("---------------")

# Crear nuevo archivo y escribir algo dentro
# El argumento es lectura/escritura
fichero = open("nombre.txt", "w+")

nombre = input("Por favor, introduzca su nombre: ")

fichero.write("Su nombre es " + nombre)

# Liberar memoria despues de escribir. Para cuando hay mucho contenido
fichero.flush()
fichero.close()

# Añadir un nuevo valor al archivo
archivo = open("nombre.txt", "a")

nombre = input("Introduzca otro nombre: ")

archivo.write("\n" + nombre)
archivo.close()

# Abrir el archivo para leer su contenido
file = open("nombre.txt", "r")
contenido = file.read()

print(contenido)

file.close()

print("FIN DEL PROGRAMA")
