#registro de datos personales y almacenarlo en un Diccionario, actualizar, eliminar, mostrar, registrar

def registrar(i):
    global usuarios
    print("\n")
    print("Registrar Usuarios".center(50, "-"))
    nombre = input("\nIngrese su nombre: ")
    apellido = (input("\nIngrese su apellido: "))
    edad = int(input("\nIngrese su edad: "))
    tel = int(input("\nIngrese su numero cel: "))
    print("\n")
    print("".center(50, "-"))

    usuarios[i] = nombre, apellido, edad, tel


def listaUsarios():
    global usuarios
    print("\n")
    print("Usuarios".center(50, "-"))
    print("\n")
    print("ID".ljust(10), "Nombre".ljust(15), "Apellidos".ljust(15), "Edad".ljust(10), "Tel")
    print("".ljust(100, "-"))
    for i in usuarios:
        print(f"{i}".ljust(10), f"{usuarios[i][0]}".ljust(15), f"{usuarios[i][1]}".ljust(15), f"{usuarios[i][2]}".ljust(10), f"{usuarios[i][3]}")
        print("".ljust(100, "-"))


def editarUsuario(num):
    global usuarios
    print("\n")
    print("Editar Usuario".center(50, "-"))
    nombre = input("\nIngrese su nombre: ")
    apellido = (input("\nIngrese su apellido: "))
    edad = int(input("\nIngrese su edad: "))
    tel = int(input("\nIngrese su numero cel: "))
    print("\n")
    print("".center(50, "-"))

    usuarios[num] = nombre, apellido, edad, tel

def eliminarUsuario(num):
    global continuar
    print("\n")
    print("Eliminar Usuario".center(50, "-"))
    global usuarios
    print("Esta seguro de eliminar el usuario con ID: {} y de Nombre: {}".format(num, usuarios[num][0]))
    duda = input("Escriba Si o NO para proceder con la operacion: ").lower()
    if duda == "si":
        del usuarios[num]
        print("\nUsuario Eliminado...")
    else:
        print(f"No se elimino el usuario {usuarios[num][0]}")
    print("\n")
    print("".center(50, "-"))


usuarios = {}
continuar = True
i = 1


while continuar == True:
    print("\n")
    print("Bienvenidos al programa".center(50, "-"))
    introducir = int(input("""
Menu de Opciones:

1.Registrar Usario
2.Listar Usuarios
3.Editar Usuario
4.Eliminar Usuario
5.salir


Ingresar una opcion: """))
    print("\n")
    print("".ljust(50, "-"))


    if introducir == 1:
        registrar(i)
        i += 1
    elif introducir == 2:
        listaUsarios()
    elif introducir == 3:
        num = int(input("Ingrese la ID del usuario a editar: "))
        editarUsuario(num)
    elif introducir == 4:
        elimina = int(input("Ingrese la ID del usuario a eliminar: "))
        eliminarUsuario(elimina)
    elif introducir == 5:
        break

