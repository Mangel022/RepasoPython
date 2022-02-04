#Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas

vocal = input("ingrese una vocal: ").lower()
letra = input("ingrese una letra: ").upper()

print(vocal, letra)
print(f"{letra.lower()}{vocal.upper()}")