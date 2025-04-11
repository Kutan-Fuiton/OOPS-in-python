# del keyword --> delete an attribute of a class object or the object itself.

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Karan")
print(s1.name)
del s1.name
print(s1.name)