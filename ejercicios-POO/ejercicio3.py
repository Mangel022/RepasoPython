#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica():

    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

class Moto(Fabrica):

    @property
    def fabricamotos(self):
        return """
        La Fabricacion de tu Moto a sido creado.

        Moto - Honda
        llantas : {}
        color : {}
        valor : {}
    """.format(self._llantas, self._color, self._precio)

class Carro(Fabrica):

    @property
    def fabricacarro(self):
        return """
        La Fabricacion de tu Moto a sido creado.

        Carro - Lamborgini
        llantas : {}
        color : {}
        valor : {}
    """.format(self._llantas, self._color, self._precio)

while True:
    print("""
        Ingrese una de las opciones.
    1.Crear Moto
    2.Crear Carro
    3.Salir
    """)
    opcion = int(input("\nIngrese su opcion: "))

    if opcion == 1:

        llantas = input("Ingrese la cantidad de llantas: ")
        color = input("Ingrese el color: ")
        precio = int(input("Ingrese el precio del vehiculo: "))

        creacionmoto = Moto(llantas, color, precio)
        print(creacionmoto.fabricamotos)
        break
    elif opcion == 2:

        llantas = input("Ingrese la cantidad de llantas: ")
        color = input("Ingrese el color: ")
        precio = int(input("Ingrese el precio del vehiculo: "))

        creacioncarro = Carro(llantas, color, precio)
        print(creacioncarro.fabricacarro)
        break
    else:
        print("\nSaliendo del programa")
        break

