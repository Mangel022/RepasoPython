#Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.

class Persona:
    
    def __init__(self):
        self._nombre = input("Introduzca su nombre: ")
        self._edad = int(input("Introduzca su edad: "))

    def imprimir(self):
        print("""
        Los datos ingresados son:
        Nombre : {}
        Edad : {}
        """.format(self._nombre, self._edad))

    def generacion(self):
        if self._edad > 0 and self._edad <= 6:
            print("Cule feto sigue chupando teta\n")
        elif self._edad > 6 and self._edad <= 12:
            print("Cule niño vacan disfruta\n")
        elif self._edad > 12 and self._edad <= 20:
            print("Los niños con anxiedad uwu\n")
        elif self._edad > 20 and self._edad <= 25:
            print("Estas en la plena juventud ponte a culear\n")
        elif self._edad > 25 and self._edad <= 60:
            print("Eres un adulto boy B)\n")
        elif self._edad > 60 and self._edad <= 60:
            print("Eres un vejestorio papi matate\n")

persona = Persona()
persona.imprimir()
persona.generacion()