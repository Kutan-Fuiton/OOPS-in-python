# del keyword --> delete an attribute of a class object or the object itself.

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Karan")
print(s1.name)
del s1.name
print(s1.name)




# Private(like) attributes and methods: we can make the attributes and methods private by using __ before the name of the attribute or method. So that it cannot be accessed outside the class. But it can be accessed inside the class. So we can use this to make the attributes and methods private. But this is not a strict rule, so we can access them outside the class also, but it is not recommended to do so. to make a attribute private just have to add two underscores ("__") before that attribute. like self.acc_pass = acc_pass, instead we will do this self.__acc_pass = acc_pass to make it private.
# Private attributes and methods are meant to be used only wihtin the class and are not accessible from outside the class.


class Account: 
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account ("12345","abcde")
print(acc1.acc_no)
# print(acc1.acc_pass)
print(acc1.reset_pass())


class Person:
    __name = "anonymous" # private attribute

    # private method
    def __hello(self):
        print("Hello Person!")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())