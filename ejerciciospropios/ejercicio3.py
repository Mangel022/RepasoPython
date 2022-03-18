#Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulo:

    def __init__(self):
        self._lado1 = int(input("Introduzca la cantidad del lado 1: "))
        self._lado2 = int(input("Introduzca la cantidad del lado 2: "))
        self._lado3 = int(input("Introduzca la cantidad del lado 3: "))

    def imprimir(self):
        print("""
    El usuario a digitalizado:

lado 1 : {}
lado 2 : {}
lado 3 : {}
""".format(self._lado1, self._lado2, self._lado3))

    def tipo_triangulo(self):
        if self._lado1 == self._lado2:
            if self._lado1 == self._lado3:
                print("Triangulo Equilatero\n")
            elif self._lado1 != self._lado3:
                print("Triangulo isoceles\n")

        elif self._lado2 == self._lado3:
            if self._lado2 == self._lado1:
                print("Triangulo Equilatero\n")
            elif self._lado2 != self._lado1:
                print("Triangulo isoceles\n")

        elif self._lado3 == self._lado1:
            if self._lado3 == self._lado2:
                print("Triangulo Equilatero\n")
            elif self._lado3 != self._lado2:
                print("Triangulo isoceles\n")

        else:
            print("Triangulo Escaleno\n")

triangulo = Triangulo()
triangulo.imprimir()
triangulo.tipo_triangulo()