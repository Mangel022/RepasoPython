#Ejercicio 1

#Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    @property
    def imprimir(self):
        return "Nombre: {} \nNota: {}".format(self._nombre, self._nota)

    @property
    def nota(self):
        if self._nota >= 3:
            return "HAS APROBADO"
        else:
            return "HAS REPROBADO"


nombre = input("Introduzca su nombre: ")
nota = int(input("Introduzca su nota sin la coma decimal: "))
estudiante = Estudiante(nombre, nota)
print(estudiante.imprimir)
print(estudiante.nota)
