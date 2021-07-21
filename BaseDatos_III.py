import sqlite3

miBD=sqlite3.connect("PrimeraBase")
miCursor=miBD.cursor()
"""
miCursor.execute('''
	CREATE TABLE PRODUCTOS1 (ID INTEGER PRIMARY KEY AUTOINCREMENT,	NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))''')
"""

#inserto varios
variosRegs= [
	("Camiseta",1200,"Deportes"),
	("Jarron",1100,"Cerámica"),
	("Camión",1140,"Jugeteria"),
	("Pelota",300,"Deportes")
]

miCursor.executemany("INSERT INTO PRODUCTOS1 VALUES (null,?,?,?)",variosRegs)
miBD.commit()

miBD.close()