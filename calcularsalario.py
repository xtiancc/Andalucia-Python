print("CALCULAR SALARIO TRABAJADORES")
print("-----------------------------")

numerohoras = int(input("Introduzca número de horas trabajadas: "))
preciohora = int(input("Por favor, introduzca precio/hora: "))
kilometros = int(input("Introduzca número de Km realizados: "))
horasextra = 0
salariobase = 0
salarioextra = 0
dieta = ""
retencion = ""
salariototal = 0

# Horas extras
if (numerohoras > 36):
    # Existen
    horasextra = numerohoras - 36
    salariobase = preciohora * 36
    salarioextra = horasextra * (preciohora + 2)
else:
    # No existen
    horasextra = 0
    salarioextra = 0
    salariobase = numerohoras * preciohora

# Tipo de dieta
if (kilometros < 100):
    dieta = "DIETA LOCAL"
elif (kilometros >= 100 and kilometros <= 500):
    dieta = "DIETA NACIONAL"
else:
    dieta = "DIETA INTERNACIONAL"

# Retenciones
salariototal = salariobase + salarioextra
if(salariototal <= 250):
    retencion = "NO TIENE RETENCIÓN"
elif (salariototal >= 251 and salariototal <= 800):
    retencion = "RETENCIÓN 20%"
else:
    retencion = "RETENCIÓN 40%"

print("Número de horas: " + str(numerohoras))
print("Precio hora: " + str(preciohora))
print("Kilometros: " + str(kilometros))
print("Horas extras: " + str(horasextra))
print("Salario extra: " + str(salarioextra))
print("Salario base: " + str(salariobase))
print("Salario total: " + str(salariototal))
print("Dietas: " + dieta)
print("Retenciones: " + retencion)

print("FIN DEL PROGRAMA.")
