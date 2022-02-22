class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property
    def cuenta(self):
        return self._cuenta

    @property
    def contador(self):
        return self._contador

a = A()
#print(a._cuenta)
#print(a.cuenta()) #esta es la manera correcta con metodo GET sin el decorador @property
print(a.cuenta) #esta es la manera correcta tambien con metodo GET y con el decorador @property
print(a.contador)