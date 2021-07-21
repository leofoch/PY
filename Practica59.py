from tkinter import *
from tkinter import messagebox
import sqlite3

#--------------------------Funcionalidad---------
def conectaBD():
	miBD=sqlite3.connect("Usuarios")
	miCursor=miBD.cursor()

	try:
		miCursor.execute ('''
			CREATE TABLE USUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50),
			PASS VARCHAS(50),
			APELLIDO VARCHAR(50),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')

		messagebox.showinfo("BBDD", "Base de datos creada con exito")

	except:
		messagebox.showwarning("Atención", "La Base de datos ya existe")


def salirAPP():
	valor= messagebox.askquestion("Salir", "Deseas salir de la APP")
	if valor=="yes":
		root.destroy()


def Limpiar():
	miID.set("")
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDomicilio.set("")
	CuadroTexto.delete(1.0,END)

def Crear():
	miBD=sqlite3.connect("Usuarios")
	miCursor=miBD.cursor()
	"""
	miCursor.execute("INSERT INTO USUARIOS VALUES (NULL,'"
		+ miNombre.get()
		+ "','" + miPass.get()
		+ "','" + miApellido.get()
		+ "','" + miDomicilio.get()
		+ "','" + CuadroTexto.get(1.0,END) + "')"
		)
	"""
	#insert por parametros
	MisParametros = miNombre.get(),miPass.get(),miApellido.get(),miDomicilio.get(),CuadroTexto.get("1.0",END)
	miCursor.execute ("INSERT INTO USUARIOS VALUES (NULL,?,?,?,?,?)",(MisParametros))

	miBD.commit()
	messagebox.showinfo("BD","Registro insertado OK")

def Read():
	miBD=sqlite3.connect("Usuarios")
	miCursor=miBD.cursor()

	miCursor.execute("SELECT * FROM USUARIOS WHERE ID = " + miID.get())

	elUsuario = miCursor.fetchall()
	for user in elUsuario:
		miNombre.set(user[1])
		miPass.set(user[2])
		miApellido.set(user[3])
		miDomicilio.set(user[4])
		CuadroTexto.insert(1.0,user[5])	

	miBD.commit()


def Actualizar():
	miBD=sqlite3.connect("Usuarios")
	miCursor=miBD.cursor()
	"""
	miCursor.execute("UPDATE USUARIOS SET NOMBRE='"+ miNombre.get() +
	"',PASS='"+ miPass.get()+
	"',APELLIDO='"+ miApellido.get()+
	"',DIRECCION='"+ miDomicilio.get()+
	"',COMENTARIOS='"+CuadroTexto.get(1.0,END) + "' WHERE ID = "+ miID.get() )
	"""
	MisParametros = miNombre.get(),miPass.get(),miApellido.get(),miDomicilio.get(),CuadroTexto.get("1.0",END)
	miCursor.execute ("UPDATE  USUARIOS SET NOMBRE = ?, PASS= ? , APELLIDO = ?, DIRECCIOn = ?, COMENTARIOS = ? WHERE ID = "+ miID.get(),(MisParametros))

	miBD.commit()
	messagebox.showinfo("BD","Registro actualizó OK")


def eliminar():
	miBD=sqlite3.connect("Usuarios")
	miCursor=miBD.cursor()

	miCursor.execute("DELETE FROM USUARIOS WHERE ID = " + miID.get())

	miBD.commit()
	messagebox.showinfo("BD","Registro Eliminado OK")
#--------------------------Pantalla---------
root=Tk()

barramenu=Menu(root)
root.config(menu=barramenu, width=300, height=300)

BDmenu=Menu(barramenu,tearoff=0)
BDmenu.add_command(label="Conectar", command=conectaBD)
BDmenu.add_command(label="Salir",command=salirAPP)

Borrarmenu=Menu(barramenu,tearoff=0)
Borrarmenu.add_command(label="Borrar Campos", command=Limpiar)

Crearmenu=Menu(barramenu,tearoff=0)
Crearmenu.add_command(label="Crear", command=Crear)
Crearmenu.add_command(label="Leer",command=Read)
Crearmenu.add_command(label="Actualizar",command=Actualizar)
Crearmenu.add_command(label="Borrar", command=eliminar)

Ayudamenu=Menu(barramenu,tearoff=0)
Ayudamenu.add_command(label="Licencia")
Ayudamenu.add_command(label="Acerca de")

barramenu.add_cascade(label="BBDD",menu=BDmenu)
barramenu.add_cascade(label="Borrar",menu=Borrarmenu)
barramenu.add_cascade(label="CRUD",menu=Crearmenu)
barramenu.add_cascade(label="Ayuda",menu=Ayudamenu)

#--------------------------comienzo de campos---------
miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDomicilio=StringVar()

CuadroID = Entry(miFrame, textvariable=miID)
CuadroID.grid(row=0,column=1, padx=10, pady=10)

CuadroNombre = Entry(miFrame, textvariable=miNombre)
CuadroNombre.grid(row=1,column=1, padx=10, pady=10)
CuadroNombre.config(fg="red", justify="right")

CuadroPass = Entry(miFrame, textvariable=miPass)
CuadroPass.grid(row=2,column=1, padx=10, pady=10)
CuadroPass.config(show="?")

CuadroApellido = Entry(miFrame, textvariable=miApellido)
CuadroApellido.grid(row=3,column=1, padx=10, pady=10)

CuadroDireccion = Entry(miFrame, textvariable=miDomicilio)
CuadroDireccion.grid(row=4,column=1, padx=10, pady=10)

CuadroTexto = Text(miFrame, width=16, height=5)
CuadroTexto.grid(row=5,column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=CuadroTexto.yview)
scrollVert.grid(row=5, column=2,sticky="nsew")
CuadroTexto.config(yscrollcommand=scrollVert.set)

#--------------------------comienzo de labels---------
idLabel=Label(miFrame,text="ID:")
idLabel.grid(row=0,column=0, sticky="e", padx=10,pady=10)

NombreLabel=Label(miFrame,text="Nombre:")
NombreLabel.grid(row=1,column=0, sticky="e", padx=10,pady=10)

PassLabel=Label(miFrame,text="Pass:")
PassLabel.grid(row=2,column=0, sticky="e", padx=10,pady=10)

ApeLabel=Label(miFrame,text="Apellido:")
ApeLabel.grid(row=3,column=0, sticky="e", padx=10,pady=10)

DirLabel=Label(miFrame,text="Direccion:")
DirLabel.grid(row=4,column=0, sticky="e", padx=10,pady=10)

ComentariosLabel=Label(miFrame,text="Comentarios:")
ComentariosLabel.grid(row=5,column=0, sticky="e", padx=10,pady=10)

#--------------------------comienzo botones---------

miFrame2=Frame(root)
miFrame2.pack()

BotonCrear=Button(miFrame2,text="Create", command=Crear)
BotonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

BotonLeer=Button(miFrame2,text="read",command=Read)
BotonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

BotonUpd=Button(miFrame2,text="Update",command=Actualizar)
BotonUpd.grid(row=1,column=2,sticky="e",padx=10,pady=10)

BotonDel=Button(miFrame2,text="Delete", command=eliminar)
BotonDel.grid(row=1,column=3,sticky="e",padx=10,pady=10)




root.mainloop()