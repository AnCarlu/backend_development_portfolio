import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * from usuarios")
    print(cursor.fetchone()) #Solo devuelve el primer registro de la consulta
    print(cursor.fetchall())