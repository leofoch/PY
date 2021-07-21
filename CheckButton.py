from tkinter import*

root=Tk()

root.title("Ejemplo Check")

playa=IntVar()
montania=IntVar()
campo=IntVar()

def opcionesviaje():
    opcionEscogida=""
    if(playa.get()==1):
        opcionEscogida+=" Playa"
    if (montania.get()==1):
        opcionEscogida+=" Montaña"
    if (campo.get()==1):
        opcionEscogida+=" Campo"

    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="abaco.png")
Label(root,image=foto).pack()

frame=Frame(root).pack()

Label(frame,text="elige destinos", width=50).pack()



Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0,  command=opcionesviaje).pack()
Checkbutton(frame, text="Montaña", variable=montania, onvalue=1, offvalue=0,command=opcionesviaje).pack()
Checkbutton(frame, text="Campo", variable=campo, onvalue=1, offvalue=0,command=opcionesviaje).pack()

textoFinal=Label(frame)
textoFinal.pack()



root.mainloop()
