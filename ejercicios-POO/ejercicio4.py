#Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga "Hola...". Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por "Soy un Pulpo". Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parametro

class Marino():
    def saludo(self):
        print("Hola...")


class Pulpo(Marino):
    def saludo(self):
        print("Soy un Pulpo")


class Foca(Marino):
    def saludo(self, mensaje):
        self._mensaje = mensaje
        print(self._mensaje)

marino = Marino()
marino.saludo()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.mensajef("Hola, Soy una foca")