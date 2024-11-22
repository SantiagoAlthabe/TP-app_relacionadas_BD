# INSERTDB.PY - Insertar registros a tabla de base de datos desde un archivo .csv
#               Aplicación realizada para bases de datos SQLite3 y MariaDB
# Para la versión de trabajo con MariaDB se comentan las lineas utilizadas
#      con SQLITE3; se dejan en el texto para cotejar diferencias entre una
#      y otra tecnología.

# Importar librerias ------------------------------------------------------------
import csv              # Libreria para tratamiento archivo ".csv"
import mysql.connector  # Importar conector mysql (maria db)
# import sqlite3        # Libreria para trabajar con SQLite

# Abrir archivo ".csv" modo lectura:  handle = open ( modo "path al archivo") ---
archivo = open(r"data3.csv")
print("Abrió archivo")  # Mensaje para debugging

# Armar la tupla a partir de la lectura del archivo .csv ------------------------
filas = csv.reader(archivo,delimiter=",")
lista = list (filas)    # Crear una lista con los registros del archivo ".csv"
del (lista[0])          # Borrar registro "encabezado" de la lista
tuplaA = tuple(lista)   # Crear una tupla con la lista obtenida del ".csv"
print("Cargó la tupla") # Mensaje para debugging

# Conectar a la base de datos ---------------------------------------------------
#    Línea que se utilizó para conectar a Base de datos SQLite
#cnxSQLite = sqlite3.connect("db1.db")

#    Conectar a mysql - MariaDB
cnxMySQL = mysql.connector.connect(host="192.168.1.33",
                                   user="Usuario",
                                   passwd="Password.MDB1",
                                   database="bd1")
print ("Conectó a base de datos")  # Mensaje para debugging

# insertar tupla en la tabla ----------------------------------------------------

#  las lineas para insertar el registro que se usaron en SQLite
#cursorL= cnxSQLite.cursor()
#cursorL.executemany("INSERT INTO usuarios ('id_us','nombre','nombre1','correo','usuario','edad','fk-ciudad') VALUES (?,?,?,?,?,?,?)",tuplaA)

# insertar en la tabla de la base datos MariaDB
cursorBD = cnxMySQL.cursor()
print ("Tomó el cursor")  # Mensaje para debugging
cursorBD.executemany("INSERT INTO data3 (indice_tiempo, origen_visitantes, visitas, observaciones) VALUES (%s,%s,%s,%s)",tuplaA)
print ("Ejecutó sql")     # Mensaje para debugging
cnxMySQL.commit()
print ("Ejecutó commit")  # Mensaje para debugging
cnxMySQL.close()
print("Cerró conexión - FIN")  # Mensaje para debugging

