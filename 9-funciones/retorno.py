def entero():
    print("Este es un dato entero:")
    return 10

def decimal():
    print("Este es una dato decimal: ")
    return 99.99

def frases():
    return "Mi nombre es miguel angel"

def aseignacion():
    return 1, 2, 3, 4, 5

print(entero())
print(decimal())
print(frases())

a, b, c , d, e = aseignacion()

print(a)
print(b)