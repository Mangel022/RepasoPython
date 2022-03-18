#Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´

class Alumno:

    def __init__(self):
        self._nombre = input("Introduzca su nombre: ")
        self._nota = int(input("Introduzca la nota del estudiante: "))

    @property
    def nombre(self):
        return self._nombre

    @property
    def nota(self):
        return self._nota

    def resultado(self):
        if self.nota >= 3:
            print("El estudiante", self._nombre, "Ah aprobado la materia con nota: ", self._nota)
        else:
            print("El estudiante", self._nombre, "No aprobo la materia su nota es: ", self._nota)

alumno = Alumno()
alumno.resultado()