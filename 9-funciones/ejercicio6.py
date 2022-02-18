#Escribir una función que reciba una muestra de números en una lista y devuelva su medida.

def media(lista):
    medIa = 0
    for i in lista:
        medIa += i
    medIa /= len(lista)
    return "la media de la lista es: {}".format(medIa)

lista = [2, 2, 3, 3, 5, 7, 8, 130]
print(media(lista))