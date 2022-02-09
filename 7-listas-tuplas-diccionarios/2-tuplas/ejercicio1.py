#Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

mesesXano = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")


numeroMes = int(input("Ingresar un numero para saber el mes seleccionado: "))

numeroMes -= 1

if mesesXano[numeroMes] in mesesXano:
    print("El mes seleccionado es:",mesesXano[numeroMes])
else:
    print("Ha ingresado un numero que no cumple con los parametros de los meses del año")