#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Introdzca su edad: "))

i = 1

while i <= edad:
    print(f"ha cumplido {i} de edad")
    i += 1
