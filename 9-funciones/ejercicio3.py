#Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0

def devolverNum(i, x):

    if i > x:
        return 1
    elif i == x:
        return 0
    else:
        return -1

num1 = int(input("Introduzca el primer numero: "))
num2 = int(input("Introduzca segundo numero: "))
print(devolverNum(num1, num2))