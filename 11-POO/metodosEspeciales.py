class FabricaTelefonos():
    def __init__(self, marca, color): #constructor
        self.marca = marca
        self.color = color
        print("El objetivo {} ha sido creado".format(self.marca))

    def __str__(self): #mensaje mas descriptivo
        return "El objeto {}".format(self.marca)

    def __del__(self): #destructor
        print("El objeto {} ha sido destruido".format(self.marca))

telefono = FabricaTelefonos("samsung", "negro")
print(telefono.marca)
print(telefono)