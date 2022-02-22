class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property
    def cuenta(self):
        return self._cuenta

    @cuenta.setter
    def cuenta(self , cuenta):
        self._cuenta = cuenta

    @property
    def contador(self):
        return self._contador

    @contador.setter        #cuando no tiene metodo setter se le conoce como redonly osea solo lectura, puede faltar setter pero nunca un GETTER
    def contador(self, contador):
        self._contador = contador


a = A()
print(a.cuenta) #obtengo los datos con GET
a.cuenta = 20 #modifico los dato con SETTER
print(a.cuenta)
print(a.contador)
a.contador = 30
print(a.contador)
#modificacion
