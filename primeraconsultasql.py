import pyodbc

print("PRIMERA CONSULTA SQL")
print("--------------------")

servidor = 'LOCALHOST\SQLEXPRESS'
bbdd = 'HOSPITAL'
user = 'sa'
password = 'azure'

cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" +
                  servidor+";DATABASE="+bbdd+";UID="+user+";PWD="+password)

print("Intentando conectar...")
conexion = pyodbc.connect(cadenaconexion)
print("CONECTADO")

cursor = conexion.cursor()
sql = 'select * from dept'
cursor.execute(sql)

for id, nombre, localidad in cursor:
    print("ID: " + str(id) + "\nNombre: " +
          nombre + "\nLocalidad: " + localidad)

cursor.close()
conexion.close()

print("FIN DEL PROGRAMA")
