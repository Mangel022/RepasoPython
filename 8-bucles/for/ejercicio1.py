#Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras

print("""
Este es el rango de numeros del 1 al 10 """)

for i in range(1, 11):
    print(i)

numero1 = int(input("Introduzca el primer numero donde quiere que empiece el rango: "))
numero2 = int(input("Introduzca el segundo numero donde quiere que termine el rango: "))

numero2 += 1

print("Este es el rango introducido por el usuario")
for i in range(numero1, numero2):
    print(i)