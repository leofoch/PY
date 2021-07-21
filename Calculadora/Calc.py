from tkinter import*

raiz= Tk()

miFrame=Frame(raiz)
miFrame.pack()

operacion=""
resultado=0

#--------------pantalla--------------------------

numeroPantalla=StringVar()
ecuacionPantalla=StringVar()

ecuacion=Entry(miFrame,textvariable=ecuacionPantalla)
ecuacion.grid(row=0,column=1,padx=10,pady=10,columnspan=4)
ecuacion.config(background="blue", fg="#03f943", justify="right")
ecuacionPantalla.set("")


pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")
numeroPantalla.set("0")



#--------------Pulsaciones teclado----------------
def numeroPulsado(num):
    currentnum=numeroPantalla.get()
    global operacion
    if operacion!="" or operacion=="igual":
        numeroPantalla.set(num)
        operacion=""
    else:
        if not(num=="," and "." in currentnum):
            if currentnum == "0" and num!=".":
                numeroPantalla.set(num)
            elif currentnum == "" and num==".":
                numeroPantalla.set("0.")
            else:
                numeroPantalla.set(numeroPantalla.get()+ num)

#--------------Funcion suma----------------
def suma(num):
    global operacion
    global resultado

    ecuacionPantalla.set(ecuacionPantalla.get()+num+"+")
    resultado+=float(num) #resultado=resultado+float(num)
    operacion="suma"
    numeroPantalla.set(resultado)
    

    #numeroPantalla.set(eval("1+2*3"))

#--------------Funcion igual----------------
def igual():
    global resultado
    global operacion
    
    operacion="igual"

    numeroPantalla.set(resultado+float(numeroPantalla.get()))
    resultado=0

    
#--------------Fila 1--------------------------
boton7=Button(miFrame,text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/", width=3, command=lambda:numeroPulsado("4"))
botonDiv.grid(row=2,column=4)


#--------------Fila 2--------------------------
boton4=Button(miFrame,text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonMul=Button(miFrame,text="x", width=3, command=lambda:numeroPulsado("4"))
botonMul.grid(row=3,column=4)

#--------------Fila 3--------------------------
boton1=Button(miFrame,text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
botonMul=Button(miFrame,text="-", width=3, command=lambda:numeroPulsado("4"))
botonMul.grid(row=4,column=4)

#--------------Fila 4--------------------------
boton0=Button(miFrame,text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
botonDec=Button(miFrame,text=",", width=3, command=lambda:numeroPulsado("."))
botonDec.grid(row=5,column=2)
botonIgual=Button(miFrame,text="=", width=3, command=lambda:igual())
botonIgual.grid(row=5,column=3)
botonSum=Button(miFrame,text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5,column=4)

#--------------Entrada datos--------------------------




raiz.mainloop()
