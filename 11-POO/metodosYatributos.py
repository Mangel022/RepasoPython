class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        return "Estas escuchand musica"

telefono = FabricaTelefonos()
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento

print(telefono.llamar("Hola, con quien hablo"))
print(telefono.escucharMusica())