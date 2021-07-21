class Coche():
    def __init__(self): #constructor
        self.largoChasis=250
        self.anchoChasis=120
        self.__ruedas=4 #encapsulamiento --> no se puede acceder desde el exterior. Si adentro
        self.__enmarcha=False #encapsulamiento --> no se puede acceder desde el exterior. Si adentro
        self.Luces = "Prendidas"

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            check = self.__chequeo()

        if(self.__enmarcha and check):
            return "El coche esta en marcha"
        elif(self.__enmarcha and check==False):
            return "Algo fallo en el chequeo"
        else:
            return "EL coche esta parado"

    def estado(self):
        print("el coche tiene " ,self.__ruedas, " ruedas.")

    def __chequeo(self):
        print("realizando Chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        if(self.gasolina=="ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False

        
class Lancha():
    eslora=500
    manga=250
    puntal=100
    enmarcha=False

    def arrancar(self):
        self.enmarcha=True

    def apagar(self):
        self.enmarcha=False

    def estado(self):
        if(self.enmarcha):
            return "La Lancha esta en marcha"
        else:
            return "La lancha esta apagada"
        
        
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()


miLancha=Lancha()
print("Manga: ", miLancha.manga, " CM")
miLancha.arrancar()
miLancha.apagar()
print (miLancha.estado())

print("----------------Creamos el objeto 2")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.__ruedas = 5 #Por estar encapsulada ignora esta linea. no da error
miCoche2.estado()
miCoche2.arrancar(False)
