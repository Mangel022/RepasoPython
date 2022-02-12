#Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

def pedirNum():
    x = 1

    while x <= 5:
        numeros = int(input("Ingrese un numero: "))
        listaNumeros.append(numeros)

        if x >= 5:
            x = int(input("""
Desea continuar?
1.si
2.no

introduzca el numero: """))
            if x == 2:
                break
        else:
            x +=1

def ListarNumeros():

    global listaNumeros

    for i in listaNumeros:
        if i%2 == 0:
            listaPar.append(i)
        else:
            listaImp.append(i)

    print("Numeros pares: ",listaPar)
    print("\nNumeros Impares: ", listaImp)



listaNumeros = []
listaPar = []
listaImp = []

sigue = True

while sigue == True:

    print("""
    Opciones de usuario:
1.Agregar un nuevos numeros
2.Listar los numeros
3.Cancelar el programa
""")

    opcion = int(input("\nIngrese el numero de las opciones: "))

    if opcion == 1:
        pedirNum()
    elif opcion == 2:
        ListarNumeros()
    elif opcion == 3:
        break

print("hola".r)
