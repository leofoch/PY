import pickle

lista_nombres=["Pedro","Ana","Lisa","Mica"]

fichero_binario=open("lista_nombres","wb")

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()

del (fichero_binario) #lo borra de a memoria
    
