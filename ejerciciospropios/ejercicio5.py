""" Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones

Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda """

class Agenda:

    def __init__(self):
        #se crea una lista
        self._contactos = []

    #menu del programa
    def menu(self):
        print("""
    Agenda Persona

1. Añadir contacto
2. Listar contactos
3. Buscar coontactos
4. Editar contactos
5. Cerrar agenda

        """)
        opcion = int(input("> "))

        if opcion == 1:
            self.añadir()
        elif opcion == 2:
            self.listar()
        elif opcion == 3:
            self.buscar()
        elif opcion == 4:
            self.editar()
        elif opcion == 5:
            print("Saliendo del programa...")
            exit()

        #llamar al menu para no salir del programa
        self.menu()

    def añadir(self):
        print("".ljust(20,"-"))
        print("Añadir Contactos".ljust(20))
        print("".ljust(20,"-"))
        nombre = input("Introduzca el nombre: ")
        cel = int(input("Introduzca el cel: "))
        email = input("Introduzca el email: ")
        self._contactos.append({'Nombre': nombre, 'Cel': cel, 'Email': email})

    def listar(self):
        print("".ljust(20,"-"))
        print("Listar Contactos".ljust(20))
        print("".ljust(20,"-"))
        if (self._contactos) == 0:
            print("No se han añadido contactos")
        else:
            print("ID".ljust(20),"Nombre")
            for x in range(len(self._contactos)):
                print("\n",x,"".ljust(18),self._contactos[x]['Nombre'])

    def buscar(self):
        print("".ljust(20,"-"))
        print("Buscar Contactos".ljust(20))
        print("".ljust(20,"-"))
        nombre = input("Introduzca el nombre que desea buscar: ")
        for x in range(len(self._contactos)):
            if nombre == self._contactos[x]['Nombre']:
                print("Datos del contacto")
                print("Nombre: ",self._contactos[x]['Nombre'])
                print("Cel: ",self._contactos[x]['Cel'])
                print("Email: ",self._contactos[x]['Email'])
                return x

    def editar(self):
        print("".ljust(20,"-"))
        print("Editar Contactos".ljust(20))
        print("".ljust(20,"-"))
        data = self.buscar()
        condition = False
        while condition == False:
            print("""
                Selecciona la opcion que deseas editar

            1. Nombre
            2. Cel
            3. Email
            4. Volver
                  """)

            opcion = int(input("> "))
            if opcion == 1:
                nombre = input("Introduzca el nombre: ")
                self._contactos[data]['Nombre'] = nombre
            elif opcion == 2:
                cel = int(input("Introduzca el numero celular: "))
                self._contactos[data]['Cel'] = cel
            elif opcion == 3:
                email = input("Introduzca el email: ")
                self._contactos[data]['Email'] = email
            else:
                condition = True

agenda = Agenda()
agenda.menu()