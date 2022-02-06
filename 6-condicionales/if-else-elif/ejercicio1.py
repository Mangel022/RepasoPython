#Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

letra = input("Introduzca una letra: ").lower()

"""
if letra == "a":
    print("la letra '{}' introducida es una vocal".format(letra))
elif letra == "e":
    print("la letra '{}' introducida es una vocal".format(letra))
elif letra == "i":
    print("la letra '{}' introducida es una vocal".format(letra))
elif letra == "o":
    print("la letra '{}' introducida es una vocal".format(letra))
elif letra == "u":
    print("la letra '{}' introducida es una vocal".format(letra))
else:
    print("la letra '{}' introducida no es una vocal".format(letra)) """

if letra in "aeiou":
    print("es una vocal")
else:
    print("no es una vocal")

