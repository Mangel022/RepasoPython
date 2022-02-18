""" class FabricaTelefonos():
    marca = "Samsung"

    def ElaborarHuawei(self): #self sirve para englobar un atributo a toda la clase
        self.marca = "Huawei"

telefono = FabricaTelefonos()
telefono.ElaborarHuawei()
print(telefono.marca) """

class FabricaTelefonos():
    def __init__(self, marca, color): #__init__ metodo constructor, para cnstruccion de atributos
        self.marca = marca
        self.color = color


telefono = FabricaTelefonos("samsung", "blanco")
print(telefono.marca)