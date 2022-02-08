#En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

#[20, 50, "Curso", 'Python', 3.14]

lista = [20, 50, "Curso", 'Python', 3.14]

print("Estos son los datos usuario", lista)
dato1 = input("\nIngrese un dato para sustituir el primer dato: ")
lista[0] = dato1
dato2 = input("\nIngrese un dato para sustituir el segundo dato: ")
lista[1] = dato2

print(lista)





