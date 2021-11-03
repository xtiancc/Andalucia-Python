import pyodbc

print("INCREMENTAR SALARIO EMPLEADOS")
print("-----------------------------")

servidor = 'LOCALHOST\SQLEXPRESS'
bbdd = 'HOSPITAL'
user = 'sa'
password = 'azure'
cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" +
                  servidor+";DATABASE="+bbdd+";UID="+user+";PWD="+password)

print("Conectando...")
conexion = pyodbc.connect(cadenaconexion)

cursor = conexion.cursor()
sqloficios = "select distinct oficio from emp"
cursor.execute(sqloficios)
print("Departamentos disponibles: ")
for ofi in cursor:
    print(ofi.oficio)
cursor.close()

oficio = input("Por favor, seleccione el oficio: ")
incremento = input("Por favor, seleccione el incremento: ")

cursor = conexion.cursor()
sqlupdate = "update emp set salario+="+incremento+" where oficio='"+oficio+"'"
cursor.execute(sqlupdate)
print("Registros modificados: " + str(cursor.rowcount))
cursor.commit()
cursor.close()

cursor = conexion.cursor()
sqlafectado = "select apellido, oficio, salario from emp where oficio='"+oficio+"'"
cursor.execute(sqlafectado)

for persona in cursor:
    print("Apellido: " + persona.apellido + "\nOficio: " +
          persona.oficio + "\nSalario actual: " + str(persona.salario))

cursor.close()
conexion.close()
