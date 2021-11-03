import pyodbc

print("ALTA ENFERMOS")
print("-------------")

servidor = 'LOCALHOST\SQLEXPRESS'
bbdd = 'HOSPITAL'
user = 'sa'
password = 'azure'
cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" +
                  servidor+";DATABASE="+bbdd+";UID="+user+";PWD="+password)

conexion = pyodbc.connect(cadenaconexion)

print("Listado actual de enfermos:")

cursor = conexion.cursor()
sqlenfermos = "select inscripcion, apellido from enfermo"
cursor.execute(sqlenfermos)
for enfermo in cursor:
    print(enfermo.inscripcion + " - " + enfermo.apellido)
cursor.close()

num = int(input("Seleccione nº paciente: "))

cursor = conexion.cursor()
sqldelete = "delete from enfermo where inscripcion=?"
cursor.execute(sqldelete, (num))
print("Registros eliminados: " + str(cursor.rowcount))
cursor.commit()
cursor.close()

print("Se ha dado el alta al paciente nº" + str(num))

conexion.close()

print("FIN DEL PROGRAMA.")