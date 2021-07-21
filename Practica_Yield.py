def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento #reemplaza el 2do bucle y devuelve las letras

ciudades_devueltas=devuelve_ciudades("CABA","Rosario","Santa Fe", "MDQ")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
