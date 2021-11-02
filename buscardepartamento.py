import pyodbc

print("BUSQUEDA DE DEPARTAMENTO")
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

dept = input("Indique número de departamento: ")

sql = 'select dept_no, dnombre, loc from dept where dept_no=' + dept
cursor = conexion.cursor()
cursor.execute(sql)

row = cursor.fetchone()

if(not row):  # También row == None
    print("Ese departamento no existe")
else:
    print("\n------------------------------\nID: " + str(row.dept_no) + "\nNombre: " +
          row.dnombre + "\nLocalidad: " + row.loc + "\n------------------------------\n")

cursor.close()
conexion.close()

print("FIN DEL PROGRAMA")
