#Conexión a la base de datos SQLite

#Modulo que permite la conexión con SQLite
import sqlite3

#En esta variable debe aparecer la ruta donde va a estar almacenada nuestra bbdd
con =sqlite3.connect("sqlite/app.db") #En caso de que el archivo no exista, python lo creará por nosotros

#Siempre se debe cerrar la base de datos, de lo contrario no podremos volver a escribir en ella
con.close()
