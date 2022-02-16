#Listar datos de empresas, agregar, eliminar, actualizar

def agregar():
    global listaEmpresas
    cantidad = int(input("\nIngrese la cantidad de empresas a listar: "))
    for i in range(cantidad):
        empresas = input(f"Ingresa el nombre de la empresa {i}: ")
        listaEmpresas.append(empresas)

def read(num):
    global listaEmpresas
    print("".rjust(20, "."),listaEmpresas[num],"\n")

def actualizar(num):
    global listaEmpresas
    updateEmpresa = input(f"Va actualizar la empresa {listaEmpresas[num]} por: ")
    listaEmpresas[num] = updateEmpresa
    print("Los cambios se han actualizado con exito...")
    print("".rjust(20, "."),listaEmpresas[num],"\n")

def eliminar(num):
    global listaEmpresas
    for i in range(len(listaEmpresas)):
        if i == num:
            respuesta = int(input(f"""
Estas seguro de eliminar la Empresa {listaEmpresas[i]} ??

1.Si
2.no

Ingrese un numero: """))
            if respuesta == 1:
                listaEmpresas.remove(listaEmpresas[i])
            else:
                break

def allista():
    global listaEmpresas
    for i in range(len(listaEmpresas)):
        print("\n",i,"-",listaEmpresas[i])

listaEmpresas = []

continuar = True
while continuar == True:
    print("Bienvenido Usuario".center(50, "-"))
    opciones=int(input("""                                                  |
Este es el menu de Opciones.                      |
--------------------------------------------------+
1.Agregar Empresas                                |
2.Ver una Empresa de la lista                     |
3.Actualizar Empresa                              |
4.Eliminar Empresa                                |
5.Listar todas las Empresas                       |
6.Salir del programa                              |
--------------------------------------------------+
Ingresa un numero de las opciones: """))

    if opciones == 1:
        agregar()
    elif opciones == 2:
        num = int(input("\nIngrese un numero para ver la empresa: "))
        read(num)
    elif opciones == 3:
        num = int(input("\nIngrese el numero de la empresa para actualizar: "))
        actualizar(num)
    elif opciones == 4:
        num = int(input("Ingrese el numero representate de la Empresa: "))
        eliminar(num)
    elif opciones == 5:
        allista()
    elif opciones == 6:
        break