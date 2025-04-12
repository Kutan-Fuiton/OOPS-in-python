# __init__():  It is a constructor. Here s1 is an object created from the class Student, now there is always a init function which when a object is created that function is called, so if there isnt any defined init function then also it wii be called, but it will not do anything, so we can define our own init function to do some work when the object is created, to create init funtion we need to give a "self" argument which basically the object itself and we can use that object as self under init function. now the argument self could be written as self or it could be named as any other thing.

# fullname is a parameter which we can use to pass the name of the student when we create the object, so we can use that name to do some work under init function.

# There are two types of constructors: default constructor and parameterized constructor. Default constructor is the one which does not take any parameters, and parameterized constructor is the one which takes parameters. So we can create a default constructor and a parameterized constructor in the same class. if parameters are given then always parameterized constructor will be called, if not then default constructor will be called.

# Anything defined inside the class is called class attribute, and anything defined inside the init function is called object attribute. So we can use class attributes and object attributes in the same class. Always object attributes will be given priority over class attributes. So if we have a class attribute and an object attribute with the same name, then the object attribute will be used.

class Student:
    college_name="ABC College" # this is class attribute
    name = "anonymous" # this is also class attribute

    # Default constructors
    def __init__(self):
        pass

    # parameterized constructors
    def __init__(self, name, marks):
        self.name = name # this is object attribute
        self.marks = marks # this is also object attribute
        print("adding new student in Database..")

s1 = Student("karan",97)
print(s1.name, s1.marks) # karan 97
print(s1.college_name) # ABC College

s2 = Student("arjun",88)
print(s2.name, s2.marks) # arjun 88
print(s2.college_name) # ABC College