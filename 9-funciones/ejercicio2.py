def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print(f"El factorial de {num}! = {fact}")

num = int(input("Introduzca un numero para conocer su factorial: "))
factorial(num)