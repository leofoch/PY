"""
def area_triangulo(base, altura):
	return (base*altura)/2


print(area_triangulo(5,7))

triangulo1 =area_triangulo(5,7)
triangulo2=area_triangulo(5,7)

print(triangulo1)
print(triangulo2)
"""
# lambda no es para funcionaes complejas. Solo para algun calculo
area_triangulo=lambda base,altura: (base*altura)/2

print(area_triangulo(5,7))

destacar_valor=lambda comision:"¡{}! $".format(comision)
comision_ana=15585
print(destacar_valor(comision_ana))