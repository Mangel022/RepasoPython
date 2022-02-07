#En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

#[20, 50, "Curso", 'Python', 3.14]

lista = [20, 50, "Curso", 'Python', 3.14]

print("Estos son los datos usuario", lista)
dato1 = input("\nIngrese un dato para sustituir el primer dato: ")
lista[0] = dato1
dato2 = input("\nIngrese un dato para sustituir el segundo dato: ")
lista[1] = dato2

if dato1[0] in "abcdefghijklmnopkrstuvwxyz":
dato2[0] in "abcdefghijklmnopkrstuvwxyz":
    print("Estos son los datos actualizados de la lista: ",lista)
else:
    lista[0] = int(dato1)
    lista[1] = int(dato2)
    print("Estos son los datos actualizados de la lista: ",lista)





