import sqlite3

con = sqlite3.connect("sqlite/app.db")

#Este objeto es necesario para poder realizar consultas SQL
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50) )
    ''')

con.commit() #Sin esta sentencia la consulta anterior no se ejecutará
con.close()