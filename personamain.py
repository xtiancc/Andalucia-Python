from persona import Persona

print("CLASE PERSONA")
print("-------------")

person = Persona()
person.nombre = "Alumno"
person.apellido = "Azure"
person.fechanacimiento = 1995

print(person.nombreCompleto())
print(str(person.getEdad()))

print(person.pais)
person.pais = "España"
print(person.pais)

print(person)

print(person.getDescripcion("eres un buen estudiante. "))
