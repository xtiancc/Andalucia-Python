import pyodbc

print("INSERTAR UN DEPARTAMENTO")
print("------------------------")

servidor = 'LOCALHOST\SQLEXPRESS'
bbdd = 'HOSPITAL'
user = 'sa'
password = 'azure'

cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" +
                  servidor+";DATABASE="+bbdd+";UID="+user+";PWD="+password)

print("Intentando conectar...")
conexion = pyodbc.connect(cadenaconexion)
print("CONECTADO")

num = input("Introduzca un número: ")
nombre = input("Inserte nombre del departamento: ")
loc = input("Indique la localidad del departamento: ")

sql = "insert into dept values ("+num+", '"+nombre+"', '"+loc+"')"
print(sql)
cursor = conexion.cursor()
cursor.execute(sql)

# Para que se guarden los cambios en SQL
cursor.commit()

cursor.close()
conexion.close()

print("FIN DEL PROGRAMA")
