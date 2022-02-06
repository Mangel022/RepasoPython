#Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese una palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("los caracteres tienen menos de 3")
elif palabra1[-3:] == palabra2[-3:]:
    print("las palabras riman")
elif palabra1[-2:] == palabra2[-2:]:
    print("las palabras riman poco")
else:
    print("las palabras no riman")