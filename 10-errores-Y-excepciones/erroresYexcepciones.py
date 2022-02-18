while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print("Su edad es: ", edad)
        break
    except:
        print("Ingreso una respuesta erronea")
    finally: #se ejecutara tenga o no tenga error
        print("L ejecucion a terminado")