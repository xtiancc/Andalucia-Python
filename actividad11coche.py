class Coche:
    marca = ""
    modelo = ""
    velocidad = 0
    encendido = False

    def arrancar(self):
        if (self.velocidad == 0 and self.encendido == False):
            print("Ha arrancado el coche.")
            self.encendido = True
        else:
            print("El coche ya está arrancado.")

    def acelerar(self):
        if (self.encendido == True):
            self.velocidad += + 5
            print("Velocidad actual: " + str(self.velocidad))
        else:
            print("No es posible aumentar la velocidad. ¿Ha arrancado su coche?")

    def frenar(self):
        if (self.velocidad > 0):
            self.velocidad -= 5
            print("Velocidad actual: " + str(self.velocidad))
        else:
            print(
                "No es posible seguir frenando. ¿Ha comprobado la velocidad de su coche?")
            print("Velocidad actual: " + str(self.velocidad))

    def detener(self):
        if (self.velocidad == 0 and self.encendido == True):
            print("Ha parado el coche.")
        else:
            print(
                "No puede detener el coche. Compruebe su velocidad o si previamente lo ha encendido.")
            print("Velocidad actual: " + str(self.velocidad))
