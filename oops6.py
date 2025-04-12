# Inheritance --> When one class(child/derived) derives the properties and methods of another class(parent/base).

# Syntax: 
# class ParentClass:
#      ......
# class ChildClass(ParentClass):
#      ......



# There are three types of inheritance:

# 1. Single Inheritance: One class inherits from another class.
# For Example:-

class Car:
    color = "red"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
print(car1.color)


# 2. Multilevel Inheritance: One class inherits from another class, which in turn inherits from another class.
# For example:-

class Car:
    color = "red"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()


# 3. Multiple Inheritance: One class inherits from multiple classes.
# For example:-

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC) 
print(c1.varB)
print(c1.varA)




# Super() function: The super() function is used to call the parent class methods and properties. super() method is used to access methods of the parent class.
# For example:-

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        #self.type = type # here if this is not defined then it will show error as type is not defined in the child class. But i need to use the parent class type. So i will use super() method to access the parent class type.
        super().__init__(type)
        super().start()

car1 = ToyotaCar("prius","electric")
print(car1.type)