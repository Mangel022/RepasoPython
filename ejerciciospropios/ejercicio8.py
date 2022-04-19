#En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.

#Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.

#La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.

#CLASE CLIENTE
class Cliente:
    def __init__(self):
        self._clientes = {}

    def login(self):
        print("Login clientes")
        nombre = input("Ingrese su nombre: ")
        cantidad = int(input("Ingrese la cantidad de dinero: "))
        self._clientes.setdefault(nombre, cantidad)

        self.comprobacion()

    def comprobacion(self):
        print("Tiene cuenta cliente?\n1.Si.\n2.No.\n3Salir.")
        opcion = int(input("> "))
        if opcion == 1:
            print("\nIniciar sesion")
            nombrec = input("Ingrese su nombre: ")
            self.nombrecli = nombrec
            if self.nombrecli in self._clientes:
                print(f"\nBienvenido {self.nombrecli}")
                print("Desea ingresar al menu?\n1.Si\n2.No")
                opcion = int(input("> "))
                if opcion == 1:
                    self.menu()
                    return self.nombrecli
                else:
                    print("\nCerrando sesion...")
                    self.login()
            else:
                print("No se encuentra en la base de datos...")
                self.login()
        elif opcion == 2:
            print("Ingresando al registro de cliente")
            self.login()
        elif opcion == 3:
            print("Saliendo del programa...")
            exit()

    def menu(self):
        print("Cliente : {}".format(self.nombrecli))
        print("""
1.Depositar.
2.Extraer.
3.Mostrar Saldo.
4.Salir.""")
        opcion = int(input("> "))

        if opcion == 1:
            self.deposito()
        elif opcion == 2:
            self.extraer()
        elif opcion == 3:
            self.mostrar()
        elif opcion == 4:
            self.comprobacion()

        self.menu()


    def deposito(self):
        print("Bienvenido al deposito {}".format(self.nombrecli))
        cantidad = int(input("Cuanto dinero desea depositar? "))
        for key in self._clientes:
            if self.nombrecli == key:
                self._clientes[key] += cantidad

    def extraer(self):
        print("Bienvenido al deposito {}".format(self.nombrecli))
        cantidad = int(input("Cuanto dinero desea retirar? "))
        for key in self._clientes:
            if self.nombrecli == key:
                self._clientes[key] -= cantidad

    def mostrar(self):
        print("Mostrando saldo de")
        for key in self._clientes:
            if self.nombrecli == key:
                print('{} su saldo es: {}'.format(self.nombrecli, self._clientes[key]))

#CLASE BANCO
class Banco(Cliente):
    def __init__(self):
        pass

#objeto constructor
cliente = Cliente()
cliente.comprobacion()

