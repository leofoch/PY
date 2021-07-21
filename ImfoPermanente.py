import pickle

class Persona:

    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("se creo una persona nueva con el mobre: ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
    personas=[]

    def __init__(self):
        listaDePersonas=open("FicheroExterno","ab+")
        listaDePersonas.seek(0)
        try:
            self.personas=pickle.load(listaDePersonas)
        except:
            print ("El fichero esta vacio")
        finally:
            print("finally")
            listaDePersonas.close()
            del(listaDePersonas)
            
    def agregarPersonas(self,p):
        print("Agrego")
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
                
    def mostrarPersonas(self):
        for i in self.personas:
            print(i)
            
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("FicheroExterno","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def MostrarInfoFicheroExterno(self):
        print("la info del Fichero es la siguiente: ")
        for p in self.personas:
            print(p)

class ArchivoFuente:
    lineasFuente=[]

    def __init__(self):
        listaFuente=open("FicheroFuente.txt","r")
        
        try:
            self.lineasFuente=listaFuente.readlines()
        except:
            print ("El fichero fuente esta vacio")
        finally:
            print("finally")
            listaFuente.close()
            del(listaFuente)
        print(self.lineasFuente[0])

miFuente=ArchivoFuente()
miLista=ListaPersonas()
for i in miFuente.lineasFuente:
    persona=miFuente.lineasFuente[0]
#persona=Persona("Juan","Masculino",78)
    miLista.agregarPersonas(persona)
    miLista.guardarPersonasEnFicheroExterno()
    miLista.MostrarInfoFicheroExterno()


#p=Persona("Ana","Femenino",33)
#miLista.agregarPersonas(p)

#p=Persona("lia","Femenino",19)
#miLista.agregarPersonas(p)

#p=Persona("Juan","Masculino",78)
#miLista.agregarPersonas(p)

#miLista.mostrarPersonas()


