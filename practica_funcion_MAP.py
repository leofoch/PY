#verifica que los elementos de una secuencia cumplan una condicion y devuelve un iterador con los elementos que la cumplen
"""
def numero_par(num):
	if num % 2==0:
		return True
"""

#numeros=[17,24,7,39,8,31,92]
#print (list(filter(lambda numero_par:numero_par%2==0,numeros)))

class Empleado:
	def __init__(self,nombre,cargo,salario):
		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario	

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)


listaEmpleados=[
Empleado("Juan", "director", 7500),
Empleado("Ana", "Presi", 8500),
Empleado("Antonio", "Adm", 2500),
Empleado("Sara", "sec", 2700),
Empleado("Mario", "botones", 2100)
]

def calculo_comisiom(empleado):
	if empleado.salario < 3000:
		empleado.salario =empleado.salario*1.03
	return empleado

listaEmpleadosComision = map(calculo_comisiom, listaEmpleados)

for empleado in listaEmpleadosComision:
	print(empleado)