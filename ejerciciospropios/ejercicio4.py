#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora:
    def __init__(self):
        self._num1 = int(input("Introduzca un numero: "))
        self._num2 = int(input("Introduzca un numero: "))

    def suma(self):
        print("suma \n{} + {} = {}".format(self._num1, self._num2, self._num1+self._num2))

    def resta(self):
        print("resta \n{} - {} = {}".format(self._num1, self._num2, self._num1-self._num2))

    def multiplicacion(self):
        print("multiplicacion \n{} * {} = {}".format(self._num1, self._num2, self._num1*self._num2))

    def division(self):
        print("suma \n{} / {} = {}".format(self._num1, self._num2, self._num1/self._num2))


calculadora = Calculadora()
calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.division()