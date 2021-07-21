from tkinter import*

raiz=Tk()

raiz.title("Ventana de la primera ostia")
#raiz.resizable(0,0) #Ancho, Alto 0=False
raiz.iconbitmap("iconoInternos02.ICO")
raiz.geometry("650x350")
raiz.config(bg="blue")

miFrame=Frame(raiz,width=500,height=400)
miFrame.grid(row=0, column=0, columnspan=4)
#siempre hay que empaquetar el Frame dentro de la raiz
miFrame.pack() #Puede ser bottom/left
miFrame.config(cursor="pirate")

miFrame.config(bg="red")
#hay que darle tamaño al frame
#miFrame.config(width="450",height="200")
#Ver Packer options en la documentacion

miImagen=PhotoImage(file="icono-enviar.gif")
Label(miFrame, image=miImagen).place(x=10,y=10)

miLabel=Label(miFrame, text="Etiqueta1")
#miLabel.place(x=100,y=200)
miLabel.grid(row=0, column=0, columnspan=2)
miLabel=Label(miFrame, text="Etiqueta2")
#miLabel.place(x=100,y=200)
miLabel.grid(row=1, column=0, columnspan=2)
miLabel=Label(miFrame, text="Etiqueta3")
#miLabel.place(x=100,y=200)
miLabel.grid(row=1, column=1, columnspan=1)

i = 200
while i < 300:
    i=i+25
    Label(miFrame, text="Etiqueta"+str(i), fg="red", font=("Comic Sans MS",14)).place(x=100,y=i)



miFrameMenu=Frame()
miFrameMenu.config(bg="green")
#hay que darle tamaño al frame
miFrameMenu.config(width="350",height="50")
#Ver Packer options en la documentacion
#siempre hay que empaquetar el Frame dentro de la raiz
miFrameMenu.pack( side="top", fill="both") #Puede ser bottom/left


miFrameMenu.config(bd=15,relief="groove")
miFrameMenu.config(cursor="hand2")





raiz.mainloop() #siempre al final


    
