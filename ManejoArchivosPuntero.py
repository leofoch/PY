from io import open

#lectura y escritura
archivo_texto=open("Archivo.txt","r+")
#archivo_texto.seek(20) #ubica el puntero
#print(archivo_texto.read(25)) #25 desde donde esta el puntero

#archivo_texto.seek(len(archivo_texto.read())/2)
#archivo_texto.seek(len(archivo_texto.readline()))
##archivo_texto.write("2222")
#print(archivo_texto.read())

lista_texto=archivo_texto.readlines()
for elemento in range(len(lista_texto)):
    print(lista_texto[elemento])

lista_texto[1]=" 11111111 \n"
archivo_texto.seek(1)
archivo_texto.writelines(lista_texto)
archivo_texto.close()

