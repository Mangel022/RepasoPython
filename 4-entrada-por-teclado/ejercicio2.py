"""
Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final
"""

p1 = int(input("Ingresar nota practica 1: "))
p2 = int(input("Ingresar nota practica 2: "))
p3 = int(input("Ingresar nota practica 3: "))

ep = int(input("Ingresar nota examen parcial: "))
ef = int(input("Ingresar nota examen final: "))

pp = (p1 + p2 + p3) / 3
prom = (pp + 2*ep + 3*ef) / 6

print(f"Nota del promedio practica: {pp} \nNota promedio: {prom}")