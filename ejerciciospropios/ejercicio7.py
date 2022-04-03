#registro de pedidos de pizzeria

class Toninos:

    def __init__(self):
        self._pedidos = []


    #agregar
    def agregar(self):
        print("Agregar pedidos".center(50,"*"))
        pedido = int(input("Introduzca el numero del pedido: "))
        nombre = input("Introduzca el nombre de la persona encargada: ")
        tipopizz = input("Introduzca el nombre de la pizza: ")
        tamaño = input("Introduzca el tamaño de la pizza: ")
        costo = int(input("Introduzca el costo de la pizza: "))
        self._pedidos.append({'id':pedido, 'nombre':nombre, 'tipo pizza':tipopizz, 'tamaño':tamaño, 'costo':costo})


    #mostrar
    def mostrar(self):
        print("Lista de pedidos")
        print("Id".rjust(20),"Nombre Encargado")
        for i in zip(len(self._pedidos)):
            print(f"{self._pedidos[i]['id']}".rjust(25),f"{self._pedidos[i]['nombre']}")
    #editar
    #eliminar