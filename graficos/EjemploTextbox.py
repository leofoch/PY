from tkinter import*

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

miNombre = StringVar()

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0,column=1, padx=10, pady=5)
cuadroNombre.config(fg="red", justify="left")

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=1,column=1, padx=10, pady=5)
cuadroPassword.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1, padx=10, pady=5)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1, padx=10, pady=5)
cuadroDireccion.insert(END, 'You email here')

cuadroTextoLargo=Text(miFrame,width=16, height=5)
cuadroTextoLargo.grid(row=4,column=1, rowspan=1 , padx= 10, pady=5)

miscrollVert=Scrollbar(miFrame, command=cuadroTextoLargo.yview) #yview=vertical
miscrollVert.grid(row=4,column=2, sticky="nsew")

cuadroTextoLargo.config(yscrollcommand=miscrollVert.set)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e", padx=10, pady=5) #w:oeste, n: norte, ne:noreste

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2,column=0,sticky="e", padx=10, pady=5)

domicilioLabel=Label(miFrame, text="Domicilio de mi casa:")
domicilioLabel.grid(row=3,column=0,sticky="e", padx=10, pady=5) 

PasswordLabel=Label(miFrame, text="Password:")
PasswordLabel.grid(row=1,column=0,sticky="e", padx=10, pady=5)

TextoLabel=Label(miFrame, text="Comentarios:")
TextoLabel.grid(row=4,column=0,sticky="e", padx=10, pady=5)

def codigoBoton():
    miNombre.set("Juan")
    
botonEnvio=Button(raiz,text="Enviar", command=codigoBoton)
botonEnvio.pack()


raiz.mainloop()


