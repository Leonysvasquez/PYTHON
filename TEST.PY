#CONEXION A BD SQL

import pyodbc

server='localhost'
bd= 'Test'
usuario= 'Soporte'
contraseña='123'



conexion= pyodbc.connect('DRIVER={ODBC Drriver 17 for SQL server};SERVER='+server+';DATABASE='
+bd';UID='+usuario+';PWD='+contraseña)


print('Conexion exitosa')

