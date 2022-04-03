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
        for i in range(len(self._pedidos)):
            print(f"{self._pedidos[i]['id']}".rjust(25),f"{self._pedidos[i]['nombre']}")

    #editar informacion
    def infeditar(self):
        serch = int(input("Introduzca la ID del pedido: "))
        for i in range(len(self._pedidos)):
            if serch == self._pedidos[i]['id']:
                print("Pedido ", self._pedidos[i]['id'])
                print("Nombre ", self._pedidos[i]['nombre'])
                print("Tipo pizza ", self._pedidos[i]['tipo pizza'])
                print("Tamaño ", self._pedidos[i]['tamaño'])
                print("Costo", self._pedidos[i]['costo'])
                return x

    
    #eliminar