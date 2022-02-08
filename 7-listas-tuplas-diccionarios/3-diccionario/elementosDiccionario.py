diccionario = {'Nombre' : 'Miguel', 'Apellido' : 'Hoyos', 'Estatura' : 1.70}

print(diccionario)
print(diccionario.keys()) #*key() muestra las llaves
print(diccionario.values()) #*values() mostrar los valores

print(diccionario["Estatura"]) #llamar la llave y que imprima el valor

diccionario["Peso"] = "75 kg" #agregar valores al diccionario

print(diccionario)

diccionario["Nombre"] = "miguel" #modificar valores

print(diccionario)
