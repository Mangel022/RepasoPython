#registro de pedidos de pizzeria

class Toninos:

    def __init__(self):
        self._pedidos = []

    #menu
    def menu(self):
        print("Bienvenido")
        print("Menu".center(20,"-"))
        print("""
        1.Agregar Pedidos
        2.Lista de Pedidos
        3.Editar Pedidos
        4.Eliminar Pedidos
        5.Salir del programa""")

        opcion = int(input("> "))
        if opcion == 1:
            self.agregar()
        elif opcion == 2:
            self.mostrar()
        elif opcion == 3:
            self.editar()
        elif opcion == 4:
            self.eliminar()
        elif opcion == 5:
            print("Saliendo del programa...")
            exit()

        #regresar al menu cada que termine una accion
        self.menu()


    #agregar pedidos
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
        print("Id".ljust(20),"Nombre Encargado")
        for i in range(len(self._pedidos)):
            print(f"{self._pedidos[i]['id']}".ljust(25),f"{self._pedidos[i]['nombre']}")
        print("\nDesea ver la informacion de algun pedido?")
        print("""
        1.Si
        2.No
        """)
        opcion = int(input("> "))
        if opcion == 1:
            self.infeditar()
        elif opcion == 2:
            pass


    #editar informacion
    def infeditar(self):
        serch = int(input("Introduzca la ID del pedido: "))
        for i in range(len(self._pedidos)):
            if serch == self._pedidos[i]['id']:
                print("Pedido: ", self._pedidos[i]['id'])
                print("Nombre: ", self._pedidos[i]['nombre'])
                print("Tipo pizza: ", self._pedidos[i]['tipo pizza'])
                print("Tamaño: ", self._pedidos[i]['tamaño'])
                print("Costo: ", self._pedidos[i]['costo'])
                return i

    def editar(self):
        print("Edita pedido")
        data = self.infeditar()
        condicion = False
        while condicion == False:
            print("""
            Menu Editar

            1.Nombre Encargado
            2.Tipo de Pizza
            3.Tamaño
            4.Costo
            5.Salir
            """)
            opcion = int(input("> "))

            if opcion == 1:
                nombre = input("Introduzca el nombre de la persona encargada: ")
                self._pedidos[data]['nombre'] = nombre
            elif opcion == 2:
                tipopizz = input("Introduzca el nombre de la pizza: ")
                self._pedidos[data]['tipo pizza'] = tipopizz
            elif opcion == 3:
                tamaño = input("Introduzca el tamaño de la pizza: ")
                self._pedidos[data]['tamaño'] = tamaño
            elif opcion == 4:
                costo = int(input("Introduzca el costo de la pizza: "))
                self._pedidos[data]['costo'] = costo
            elif opcion == 5:
                break


    #eliminar
    def eliminar(self):
        print("Eliminar pedido")
        serch = int(input("Introduzca la ID del pedido: "))
        for i in range(len(self._pedidos)):
            if serch == self._pedidos[i]['id']:
                serch -= 1
                self._pedidos.remove(self._pedidos[serch])
                print("Pedido Eliminado...")
                self.mostrar()


#objeto constructor
toninos = Toninos()
toninos.menu()