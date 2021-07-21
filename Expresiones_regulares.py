import re
#https://www.youtube.com/watch?v=Q4vXCQd1zwc

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

#print(re.search("aprender",cadena))

textoBuscar = "aprender"

textoEncontrado=re.search(textoBuscar,cadena) 

print(textoEncontrado.start()) #8
print(textoEncontrado.end()) #16
print(textoEncontrado.span()) #(8, 16)



textoBuscar = "Python"
print(re.findall(textoBuscar,cadena)) #['Python', 'Python']
print(len(re.findall(textoBuscar,cadena))) #2 --> Longitud de la lista. cuantas veces aparece


"""
if re.search(textoBuscar,cadena) is not None:
	print("OK")
else:
	print("No OK")
"""

#Metacaracteres (^comienza por, Finaliza por$
lista_nombres=['Ana Gomez', 
				'Martin Pacho', 
				'Sandra Lopez', 
				'Santiago Pacho',
				'Sandra Fernandez']
"""
for elemento in lista_nombres:
	
	if re.findall('^Sandra',elemento):
		print(elemento)
	if re.findall('Pacho$',elemento):
		print(elemento)
		
	if re.findall('[gz]',elemento):
		print(elemento)
	

lista_otros=['hombres', 
				'mujeres', 
				'niños', 
				'niñas',
				'camion',
				'camión']

for elemento in lista_otros:
	if re.findall('niñ[oa]s',elemento):
		print(elemento)
	if re.findall('cami[oó]n',elemento):
		print(elemento)
"""
for elemento in lista_nombres:
	#if re.findall('^[F-T]',elemento):
	#	print(elemento)
	#if re.findall('[o-t]',elemento):
	#	print(elemento)
	#if re.findall('[o-t]$',elemento):
	#	print(elemento)
	#if re.findall('Ma[o-t]',elemento):
	#	print(elemento)
	if re.findall('M[^o-t]',elemento):  #Negacion del rango
		print(elemento)