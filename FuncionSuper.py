#Herencia con Funcion Super()

class Persona():
    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print ("Nombre: ", self.nombre,"\nEdad: ", self.edad, "\nLugar :", self.lugar_residencia)


class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_emp,edad_emp,lugar_emp):
        super().__init__(nombre_emp,edad_emp,lugar_emp) #llama al metodo init de la clase padre
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario,  "\nAntiguedad: ", self.antiguedad)

Antonio=Empleado(1500,15,"Antonio",55,"España")
Antonio.descripcion()
print(isinstance(Antonio,Persona))

pepe=Persona("Juan",44,"Argentina")
pepe.descripcion()
print(isinstance(pepe,Empleado))


