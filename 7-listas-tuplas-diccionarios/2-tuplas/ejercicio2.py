#Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa

abc = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

numAbc = int(input("Ingrese un numero para imprimir una letra del abecedario: "))

numAbc -= 1

if  abc[numAbc] in abc:
    print("Esta es la letra seleccionada del abecedario:",abc[numAbc])
else:
    print("Ingrese un numero que este en los parametros del abcdario")