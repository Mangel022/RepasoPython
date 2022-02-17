#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def iva(cantidad, iba):
    import math
    if iba == 0:
        iba = 0.21
        valorTotal = (cantidad * iba) + cantidad
        return valorTotal
    else:
        valorTotal = ((cantidad * iba) / 100) + cantidad
        return valorTotal

cantidad = float(input("Introduzca el valor: "))
iba = float(input("Introduzca el valor del iva: "))
print(iva(cantidad, iba))
