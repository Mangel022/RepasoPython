#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, realiza un programa que muestre el peso total de toda la venta.

#Pista: Suponiendo que un cliente pide 5 payasos y 3 muñecas, la juguetería debería hacer la multiplicación de la cantidad de payasos con su peso, al igual que las muñecas; al tener ambos totales de peso, se debe sumar.


payasos = 112
munecas = 75

textp = int(input('Introduzca la cantidad de payasos a comprar🤡: '))
textm = int(input('Introduzca la cantidad de payasos a muñecas🎎: '))

pesoTotalp = payasos * textp
pesoTotalm = munecas * textm
pesoTotal = pesoTotalm + pesoTotalp

print('El peso total de ventas de payasos🤡:',pesoTotalp)
print('El peso total de ventas de payasos🎎:',pesoTotalm)
print('El peso total de ambos juguetes es de:',pesoTotal)
