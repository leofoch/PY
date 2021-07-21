class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")


#miVehiculo=Moto()
#miVehiculo.desplazamiento()

#miVehiculo2=Coche()
#miVehiculo2.desplazamiento()

#miVehiculo3=Camion()
#miVehiculo3.desplazamiento()

#no las uso

def desplazamientoVehiculo(vehiculo): #aca se usa el polimorfismo
    vehiculo.desplazamiento()

miVehiculo=Coche() #puedo pasarle Coche o Camion o Moto de acuerdo a lo que quiero
desplazamientoVehiculo(miVehiculo)

