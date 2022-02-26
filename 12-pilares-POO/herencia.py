class Animales(): #clase padre
    def habla(self):
        print("yo soy un animal")

    def descripcion(self):
        print("yo soy un {}".format(self.animal))

class Perro(Animales): #clase hija
    pass

class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal

animales = Animales()
animales.habla()

perro = Perro()
perro.habla()

abeja = Abeja("abeja")
abeja.descripcion()