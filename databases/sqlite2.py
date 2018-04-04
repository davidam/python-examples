import sqlite3

conex = sqlite3.connect('productos.sqlite')
cursor = conex.cursor()

def creacion():
    cursor.execute("CREATE TABLE IF NOT EXISTS listado (" +
                   "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, " +
                   "nombre TEXT NOT NULL, " +
                   "proveedor TEXT NOT NULL, " +
                   "precio REAL, " +
                   "stock INTEGER DEFAULT 0)")

def insertar():
    nomb = input("Nombre del producto: ")
    prov = input("Proveedor: ")
    prec = input("Precio: ")
    cursor.execute("INSERT INTO listado (nombre, proveedor, precio) " +
                   "VALUES (?, ?, ?)", (nomb, prov, prec))
    conex.commit()

creacion()
insertar()
cursor.close()
