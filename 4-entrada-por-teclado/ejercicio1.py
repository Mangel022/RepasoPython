#Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
from math import sqrt

a =  int(input("Ingresar valor de A: "))
b =  int(input("Ingresar valor de B: "))
c =  int(input("Ingresar valor de C: "))
x1 = 0
x2 = 0

if ((b**2) - (4*a*c)) < 0:
    print("no se puede realizar porque no se puede sacar raiz a un numero negativo")
else:
    x1 = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)
print("La solucion es: \n x1=",x1, "\n x2=",x2)