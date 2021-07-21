#documentacion en: http://pyspanishdoc.sourceforge.net/lib/module-string.html

#nombreUsuario=input("intro nombre: ")
#print("El nombre es: ", nombreUsuario.upper())
#print("El nombre es: ", nombreUsuario.capitalize())

edad=input("intro Edad: ")

while(edad.isdigit()==False):
    print("No es numerico")
    edad=input("intro Edad: ")
    
if(int(edad)<18):   #ojo--> todo lo que introduce desde pantalla es considerado un texto. por eso se usa "int"
    print("ok")
else:
    print("NO OK")
