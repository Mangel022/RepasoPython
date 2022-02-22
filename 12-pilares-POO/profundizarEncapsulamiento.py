class A():
    def __init__(self):
        self._contador = 0 #objeto encapsulado
        self._cuenta = 0     #objeto publico

    def incrementar(self):
        self._contador += 1

    def cuenta(self):
        return self._contador

a = A()
""" print(a.cuenta)
a.cuenta = 20
print(a.cuenta) """