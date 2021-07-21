from tkinter import*
from tkinter import messagebox # para ventanas emergentes
from tkinter import filedialog # para ventanas emergentes

root=Tk()

def infoadicional():
	messagebox.showinfo("Procesador de Leo","Procesador de textos v2019")

def infolicencia():
	messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def opcionsalir():
	
	#valor=messagebox.askquestion("Salir","Deseas salir?")
	#if valor=="yes":
	#	root.destroy()
	
	valor=messagebox.askokcancel("Salir","Deseas salir?")
	if valor==True:
		root.destroy()

def opcioncerrar():
	valor=messagebox.askretrycancel("Reintentar","No es posible cerrar. Bloqueado")
	if valor==False:
		root.destroy()

def opcionabrirfile():
	fichero=filedialog.askopenfilename(title="Abrir", 
		initialdir="C:/Users/lfochtman/Documents/01/Python", 
		filetype=(
			("Ficheros de excel","*.xlsx"),
			("Ficheros de texto","*.txt"),
			("Todos","*¨*"))
		)
	print(fichero)

#Button(root,text="abrir fichero", command=opcionabrirfile).pack()


barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#Elementos
archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir",command=opcionabrirfile)
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_command(label="Cerrar",command=opcioncerrar)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=opcionsalir)
#------------------------------------------
edicionMenu=Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")
#------------------------------------------
toolsMenu=Menu(barraMenu, tearoff=0)
#------------------------------------------
ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia",command=infolicencia)
ayudaMenu.add_command(label="Acerca de", command=infoadicional)

#------------------------------------------
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=toolsMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


root.mainloop()
