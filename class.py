class Person:
    def __init__(self, n="Name", s="Surname"):
        self.name = n
        self.surname = s

p1 = Person("Bill","Ross")
print(p1.name, p1.surname)
p2 = Person("123", "321")
print(p2.name, p2.surname)
p3 = Person()
print(p3.name, p3.surname)