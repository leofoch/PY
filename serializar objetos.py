import pickle


class vehiculos():

    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca " , self.marca, 
              "\nModelo: ", self.modelo, 
              "\nEn Marcha: ", self.enmarcha, 
              "\nAcelerando: ", self.acelera, 
              "\nFrenando: ", self.frena)

class Furgoneta(vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta NO esta cargada"
   
    
class Moto(vehiculos): #La clase Moto hereda de la clase vehiculos
    hwilly=""
    def willy(self):
        self.hwilly = "Haciendo Willy"
        
    def estado(self): #sobreescritura de metodo estado (agrego el Willy)
        print("Marca " , self.marca, "\nModelo: ", self.modelo, 
              "\nEn Marcha: ", self.enmarcha,"\nAcelerando: ", self.acelera, 
              "\nFrenando: ", self.frena,"\n",self.hwilly)

class Electricos(vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100

    def cargarenergia(self):
        self.cargando=True

class BicicletaElectrica(Electricos,vehiculos): #herencia multiple. 
    pass

coche1=vehiculos("Mazda","MX5")
coche2=vehiculos("Saet","Leon")
coche3=vehiculos("Renault","Megane")

coches=[coche1,coche2,coche3]

fichero=open("loscoches","wb")
pickle.dump(coches,fichero)

fichero.close()
del(fichero)

ficheroApertura=open("loscoches","rb")
miscoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for c in miscoches:
    print(c.estado())
