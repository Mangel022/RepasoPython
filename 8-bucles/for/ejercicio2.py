#Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares

numer1 = int(input("Introduzca el primer numero del rango: "))
numer2 = int(input("Introduzca el segundo numero del rango: "))

numer2 += 1

for i in range(numer1, numer2):
    if i%2 == 0:
        continue
    else:
        print(i)