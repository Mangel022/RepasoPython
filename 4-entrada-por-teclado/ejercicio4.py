""" 
Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>
 """

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
genero = input("ingrese su sexo M/F: ")

print("Su nombre es: {}\nSu edad es: {}\nEres: {}".format(nombre, edad, genero))