""" class Animales():
    def __init__(self, nombre):
        self.nombre = nombre


class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre)
        self.sonido = sonido

perro = Perro("Firulais", "Guaaaaooo")
print(perro.nombre)
print(perro.sonido) """


#HACERLO DE LA MANERA CORRECTA

class Animales():
    def __init__(self, nombre):
        self._nombre = nombre

class Perro(Animales):
    def __init__(self, sonido):
        self._sonido = sonido

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def sonido(self):
        return self._sonido


perro = Perro("Guaooo")
perro.nombre = "firulais"
print(perro.nombre)
print(perro.sonido)