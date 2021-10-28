import random


def generarAleatorio(min, max):
    return random.randint(min, max)


def calcularMedia(num1, num2):
    return (num1 + num2) / 2


class Mes():

    name = ""
    max = 0
    min = 0
    media = 0

    def __init__(self):
        self.max = generarAleatorio(15, 30)
        self.min = generarAleatorio(5, self.max)
        self.media = calcularMedia(self.max, self.min)

    def __str__(self):
        return "\nNombre: " + self.name + "\nMáxima: " + str(self.max) + "\nMínima: " + str(self.min) + "\nMedia: " + str(self.media)
