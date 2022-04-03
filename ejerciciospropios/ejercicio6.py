#registrar id, nombre de la empresa, nit de la empresa, direcion, email, telefono

class Empresas:

    def __init__(self):
        self._registro = []

    #MENU de la aplicacion
    def menu(self):
        print("Bienvenidos a nuestra aplicacion de datos".center(50))
        print("-".rjust(50))
        print("""
        Menu

    1.Agregar Informacion de Empresas
    2.Mostrar Listado de Empresas
    3.Editar Informacion de una Empresa
    4.Eliminar Empresa
    5.Salir de la aplicacion
    """)
        option = int(input("> "))

        if option == 1:
            self.agregar()
        elif option == 2:
            self.mostrar()
        elif option == 3:
            self.editar()
        elif option == 4:
            self.eliminar()
        elif option == 5:
            print("Saliendo del programa...")
            exit()

        #luego que se realice la accion regresar automaticamente al menu
        self.menu()

    #Agregar empresas
    def agregar(self):
        print("-".center(50,"-"))
        print("Agregar Empresa".rjust(25," "))
        print("-".center(50,"-"))
        id = int(input("\nIntroduzca el id: "))
        nombre = input("Introduzca el nombre de la empresa: ")
        nit = int(input("Introduzca el NIT de la empresa: "))
        dirr = input("Introduzca la direccion: ")
        email = input("Introduzca el email: ")
        telefono = int(input("Introduzca el telefono: "))
        self._registro.append({'id':id,'nombre':nombre,'nit':nit,'direccion':dirr,'email':email,'tel':telefono})

    #mostrar las empresas en listas
    def mostrar(self):
        print("-".center(50,"-"))
        print("Lista de las Empresas".rjust(25," "))
        print("-".center(50,"-"))
        print("\n")
        print("ID".ljust(20),"Nombre de la Empresa")
        for x in range(len(self._registro)):
            print(f"{ self._registro[x]['id']}".ljust(20),f"{self._registro[x]['nombre']}")
        condicion = False
        while condicion == False:
            print("\nDesea ver la informacion de una empresa?\n1.Si\n2.No")
            opcion = int(input("> "))
            if opcion == 1:
                self.info()
                self.menu()
            else:
                self.menu()

    #mostrar informacion de una empresa
    def info(self):
        print("-".center(50,"-"))
        print("Informacion de la empresa".rjust(25," "))
        print("-".center(50,"-"))
        serch = int(input("Introduzca la id: "))
        for x in range(len(self._registro)):
            if serch == self._registro[x]['id']:
                print("ID: ",self._registro[x]['id'])
                print("Nombre de la empresa: ",self._registro[x]['nombre'])
                print("Nit de la empresa: ",self._registro[x]['nit'])
                print("Direccion: ",self._registro[x]['direccion'])
                print("Email: ",self._registro[x]['email'])
                print("Telefono: ",self._registro[x]['tel'])

    #editar informacion de una empresa (bloque de ayuda principal)1
    def editar(self):
        print("-".center(50,"-"))
        print("Editar empresa".rjust(25," "))
        print("-".center(50,"-"))
        data = self.editarsec()
        condicion = False
        while condicion == False:
            print("""
Menu Editar informacion de la empresa

1.Nombre
2.Nit
3.direccion
4.email
5.tel
6.volver
        """)
            opcion = int(input("> "))
            if opcion == 1:
                nombre = input("Introduzca el nombre de la empresa: ")
                self._registro[data]['nombre'] = nombre
            elif opcion == 2:
                nit = int(input("Introduzca el NIT de la empresa: "))
                self._registro[data]['nit'] = nit
            elif opcion == 3:
                dirr = input("Introduzca la direccion: ")
                self._registro[data]['direccion'] = dirr
            elif opcion == 4:
                email = input("Introduzca el email: ")
                self._registro[data]['email'] = email
            elif opcion == 5:
                tel = int(input("Introduzca el telefono: "))
                self._registro[data]['tel'] = tel
            else:
                print("Regresando al menu...")
                condicion = True

    #editar informacion de una empresa (bloque de ayuda) 2
    def editarsec(self):
        serch = int(input("Introduzca la id: "))
        for x in range(len(self._registro)):
            if serch == self._registro[x]['id']:
                print("ID: ",self._registro[x]['id'])
                print("Nombre de la empresa: ",self._registro[x]['nombre'])
                print("Nit de la empresa: ",self._registro[x]['nit'])
                print("Direccion: ",self._registro[x]['direccion'])
                print("Email: ",self._registro[x]['email'])
                print("Telefono: ",self._registro[x]['tel'])
                return x

    #eliminar empresa
    def eliminar(self):
        print("-".center(50,"-"))
        print("Eliminar Empresa".rjust(25," "))
        print("-".center(50,"-"))
        serch = int(input("Introduzca la ID de la empresa a eliminar: "))
        for x in range(len(self._registro)):
            if serch == self._registro[x]['id']:
                serch -= 1
                self._registro.remove(self._registro[serch])
        print("Empresa eliminada")
        self.mostrar()


empresas = Empresas()
empresas.menu()