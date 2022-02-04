#Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

""" • Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer. """

friendZone = 'Te quiero solo como amigo'

print(friendZone[0:2]) #mostrar los 2 primeros caracteres
print(friendZone[-3:]) #mostras los 3 ultimos caracteres
print(friendZone[0::2]) #mostrar la cadena cada 2 caracteres
print(friendZone[::-1]) #mostrar cadena alreves
print(friendZone + friendZone[::-1]) #mostrar cadena en un sentido y a la inversa efecto espejo