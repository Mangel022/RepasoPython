#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():

    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    @property
    def sumas(self):
        self._suma = self._num1 + self._num2
        return "La suma de: {} + {} = {}".format(self._num1, self._num2, self._suma)

    @property
    def restas(self):
        self._resta = self._num1 - self._num2
        return "La suma de: {} - {} = {}".format(self._num1, self._num2, self._resta)

    @property
    def multiplicacion(self):
        self._multiplica = self._num1 * self._num2
        return "La suma de: {} * {} = {}".format(self._num1, self._num2, self._multiplica)

    @property
    def divisiones(self):
        self._divide = self._num1 / self._num2
        return "La suma de: {} / {} = {}".format(self._num1, self._num2, self._divide)




while True:
    num1 = int(input("Ingrese un numero entero: "))
    num2 = int(input("Ingrese un numero entero: "))
    if num1 > 0 and num2 > 0:
        pcalculadora = Calculadora(num1, num2)
        print(pcalculadora.sumas)
        print(pcalculadora.restas)
        print(pcalculadora.multiplicacion)
        print(pcalculadora.divisiones)
        break
    else:
        print("Error Zero division, los numeros ingresados no se pueden dividir entre 0")