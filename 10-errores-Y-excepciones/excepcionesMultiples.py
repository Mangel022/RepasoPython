while True:
    try:
        numero = int(input("Ingrese un numero: "))
        resultado = 100 / numero
        print(resultado)
        break
    except KeyboardInterrupt:
        print("Has cancelado la ejecucion")
        break

#tipo de excepciones
#ZeroDivisionError - no se puede divir entre 0
#ValueError - si el valor establecido es erroneo
#KeyboardInterrupt - cancelar la ejecicion del programa