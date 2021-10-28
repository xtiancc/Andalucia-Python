class Persona:
    nombre = ""
    apellido = ""
    fechanacimiento = ""
    pais = ""

    def __init__(self):
        self.pais = "Francia"

    def nombreCompleto(self):
        return self.nombre + " " + self.apellido

    def getEdad(self):
        return 2021 - self.fechanacimiento

    def getDescripcion(self, midescripcion):
        return self.nombreCompleto() + ", " + midescripcion

    def __str__(self):
        return "Nombre: " + self.nombre + "\nApellido: " + self.apellido + "\nEdad: " + str(self.getEdad()) + "\nPaís: " + self.pais
