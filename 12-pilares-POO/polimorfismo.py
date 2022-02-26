class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):   #polimorfismo la modificacion de metodos de clases heredadas y tambien la ocupacion de objetos apartir de varios metodos
        print("Yo digo guauuu")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

#creando el obejto
perro = Perro("Guau")
perro.hablar()

animales = Animales("Miau")
animales.hablar()

pez = Pez("nada")
pez.hablar()