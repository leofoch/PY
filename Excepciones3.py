def evalEdad(edad):
    if edad<0:
        raise ZeroDivisioError("No se permiten edades negativas")
   
    if edad<20:
        return "Muy Joven"
    elif edad<40:
        return "un poco Joven"
    elif edad<65:
        return "Maduo"
    elif edad<100:
        return "Cuidate"


print(evalEdad(-18))
