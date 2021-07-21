from io import open

#escritura
archivo_texto=open("Archivo.txt","w")
frase="Estupendo dia? \n todo pasa."
archivo_texto.write(frase)
archivo_texto.close()

#lectura
archivo_texto=open("Archivo.txt","r")
texto=archivo_texto.read()
archivo_texto.close()
print(texto)


#lectura por linea
archivo_texto=open("Archivo.txt","r")
lineas_de_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_de_texto[0])

#Abrir para agregar info (append)
archivo_texto=open("Archivo.txt","a")
archivo_texto.write("\n espero que rapido")
archivo_texto.close()
