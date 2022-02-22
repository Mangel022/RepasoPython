class FabricaTelefonos():
    def __init__(self, marca, *colores, **modelo): # *objeto (es una tupla) **objeto(diccionario) -> como se reconoce (m1 = 500) = (key : value)
        self.marca = marca
        self.colores = colores
        self.modelo = modelo
        

telefonos = FabricaTelefonos("samsung", "Negro", "Azul", "Rojo", m1 = 500, m2 = 1000)
print(telefonos.marca)
print(telefonos.colores)
print(telefonos.modelo)
telefonos.memoria = 512
print(telefonos.memoria) #objetos temporales