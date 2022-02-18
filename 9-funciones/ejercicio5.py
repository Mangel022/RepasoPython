#Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio

def areaCuadrado(base, altura):
    area = base * altura
    return "El area de un cuadrado es: {}".format(area)

def areaCirculo(radio):
    radio/=2
    area = ((radio ** 2) * 3.14)
    return "El area de un circulo es {} cm²".format(area)

base = int(input("Introduzca la base: "))
altura = int(input("Introduzca la altura: "))
print(areaCuadrado(base, altura))
radio = int(input("Introduzca la radio del circulo: "))
print(areaCirculo(radio))