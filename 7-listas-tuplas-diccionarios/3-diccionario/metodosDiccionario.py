diccionario = {
    1 : 2,
    2 : 3,
    3 : 4
}

diccionario2 = {
    4 : 5,
    6 : 7,
    8 : 9
}
print(diccionario)
#diccionario.pop(3) #*pop(key) pasar como parametro una llave y la elimina

#diccionario.clear() #*clear() borra todo el diccionario

#print(diccionario.get(2)) #*get(key) trae el valor de el parametro que se le pasa

#diccionario.setdefault(4, 5) #*setdefault(key, value) agregar nuevos valores

diccionario.update(diccionario2) #*update(dict) unir 2 diccionarios
print(diccionario)