#importante cada vez que se usa poo

class A():
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0

    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador

print("objeto A")
a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador) #no es una buena practica

print("\nobjeto B")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador) #encapsulamiento -> para acceder al atributo de manera privada, no puede ser accedido por fuera de la clase