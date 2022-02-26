class A():
    def primera(self):
        return "CLASE A"

class B():
    def segunda(self):
        return "CLASE B"

class C(A, B): #acceder a varios metodos multiples
    pass

c = C()
print(c.primera())
print(c.segunda())