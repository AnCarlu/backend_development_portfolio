import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor= con.cursor()
    #cursor.execute(
        #'insert into usuarios values(?,?)', #Es importante separar la inserción de esta manera para evitar  SQL Inyection
        #(1, "Hola mundo")
        #)
    
    usuarios = [
        (2, "Bihurri"),
        (3, "Obito")
    ]

    cursor.executemany(
        'insert into usuarios values(?,?)',
        usuarios
    )