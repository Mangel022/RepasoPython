#Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

numero = int(input("Introduzca un numero: "))

#abs() funcion de valores absolutos

if numero > 0:
    print("El valor absoluto de: |{}| = {}".format(numero, abs(numero)))
else:
    print("El valor absoluto de: |{}| = {}".format(numero, abs(numero)))