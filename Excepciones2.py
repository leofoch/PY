
def divide():

    try:
        op1=float(input("introduce valor 1 "))

        op2=(float(input("introduce valor 2 ")))

        print("Resul: " + str(op1/op2))

    except ValueError:
        print("valor choto")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except:
        print("Ops")
        
    print("finalizado")


divide()
