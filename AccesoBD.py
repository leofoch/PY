import sqlite3

miBD=sqlite3.connect("PrimeraBase")
miCursor=miBD.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NombreArticulo varchar(50), Precio integer, Seccion varchar(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('Medias',10,'Deportes')")

#inserto varios
"""
variosRegs= [
	("Camiseta",1200,"Deportes"),
	("Jarron",1100,"Cerámica"),
	("Camión",1140,"Jugeteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosRegs)
miBD.commit()
"""
#recupero varios datos
miCursor.execute("SELECT * FROM PRODUCTOS")
variableRegs = miCursor.fetchall()
for producto in variableRegs:
	print("nombre articulo:", producto[0])


miCursor.close()
miBD.close()