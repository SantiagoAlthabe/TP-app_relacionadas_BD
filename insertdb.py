import csv
import sqlite3

archivo = open(r"\C:\Users\santi\Desktop\archivos\data.csv")

filas   = csv.reader(archivo,delimiter=";")

lista = list (filas)
del (lista[0])
tuplaa = tuple(lista)

#insertar

conexion = sqlite3.connect("csvpyinsert.db")
cursor   = conexion.cursor()
cursor.executemany("INSERT INTO usuarios ('id_us','nombre1','nombre2','correo','usuario','edad','fk_ciudad') VALUES (?,?,?,?,?,?,?)",tuplaa)

conexion.commit()
conexion.close()